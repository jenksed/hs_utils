import re
from html import escape

def validate_slug(slug):
    """
    Ensures the slug is valid for HubSpot.

    Args:
        slug (str): The slug string to validate.

    Returns:
        bool: True if the slug is valid, False otherwise.
    """
    # HubSpot slug rules: should be lowercase, no special characters except hyphens,
    # should not start or end with a hyphen, and no consecutive hyphens.
    if not slug:
        return False
    if slug != slug.lower():
        return False
    if not re.match("^[a-z0-9]+(?:-[a-z0-9]+)*$", slug):
        return False
    return True


def prepare_page_data(page_data):
    """
    Preprocesses page data before sending it to the API.

    Args:
        page_data (dict): The dictionary containing page data.

    Returns:
        dict: The processed page data ready for API submission.
    """
    # Ensure the title is properly escaped to prevent XSS attacks
    page_data['title'] = escape(page_data.get('title', 'Default Title'))

    # Clean and setup the HTML content
    html_content = page_data.get('content', '')
    # Example: Simple stripping of script tags - for demonstration purposes
    clean_html = re.sub(r'<script.*?>.*?</script>', '', html_content, flags=re.DOTALL)
    page_data['content'] = clean_html

    # Ensure the slug is valid
    slug = page_data.get('slug', '').replace(' ', '-').lower()
    if not validate_slug(slug):
        raise ValueError("Invalid slug provided.")
    page_data['slug'] = slug

    return page_data