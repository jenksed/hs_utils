import re

def validate_slug(slug):
    """
    Ensures the slug is valid for HubSpot.

    Args:
        slug (str): The slug string to validate.

    Returns:
        bool: True if the slug is valid, False otherwise.
    """
    if not slug:
        return False
    if slug != slug.lower():
        return False
    if not re.match("^[a-z0-9]+(?:-[a-z0-9]+)*$", slug):
        return False
    return True

def normalize_slug(slug):
    """
    Normalizes the input string to a slug format suitable for URLs.

    Args:
        slug (str): The string to normalize.

    Returns:
        str: A normalized slug.
    """
    return slug.replace(' ', '-').lower()
