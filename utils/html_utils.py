from html import escape
import re

def escape_html_title(title):
    """
    Escapes HTML characters in titles to prevent XSS attacks.

    Args:
        title (str): The title to escape.

    Returns:
        str: The escaped title.
    """
    return escape(title)

def clean_html_content(html_content):
    """
    Cleans HTML content to remove potentially malicious scripts.

    Args:
        html_content (str): The HTML content to clean.

    Returns:
        str: The cleaned HTML content.
    """
    return re.sub(r'<script.*?>.*?</script>', '', html_content, flags=re.DOTALL)

def prepare_page_data(page_data):
    """
    Preprocesses page data before sending it to the API.

    Args:
        page_data (dict): The dictionary containing page data.

    Returns:
        dict: The processed page data ready for API submission.
    """
    page_data['title'] = escape_html_title(page_data.get('title', 'Default Title'))
    page_data['content'] = clean_html_content(page_data.get('content', ''))

    from slug_utils import validate_slug, normalize_slug
    slug = normalize_slug(page_data.get('slug', ''))
    if not validate_slug(slug):
        raise ValueError("Invalid slug provided.")
    page_data['slug'] = slug

    return page_data
