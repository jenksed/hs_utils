import requests
from .models import HubSpotPage, HubSpotPageUpdate

class HubSpotAPI:
    """
    Main client for interacting with the HubSpot CMS API.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.hubapi.com"

    def _make_request(self, method, endpoint, params=None, data=None):
        """Handles API requests, error handling, etc."""
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.request(method, url, params=params, json=data, headers=headers)
        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            # Handle specific HTTP errors here if necessary
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

    def create_page(self, page: HubSpotPage):
        """Creates a new page in HubSpot."""
        endpoint = "/cms/v3/pages"
        if not page.validate_slug():
            raise ValueError("Invalid slug provided for the page.")
        data = {
            "name": page.name,
            "html": page.html,
            "slug": page.slug,
            "meta_description": page.meta_description,
        }
        return self._make_request("POST", endpoint, data=data)

    def update_page(self, page_update: HubSpotPageUpdate):
        """Updates an existing page in HubSpot."""
        endpoint = f"/cms/v3/pages/{page_update.id}"
        data = page_update.prepare_update_data()
        return self._make_request("PATCH", endpoint, data=data)

    def delete_page(self, page_id: int):
        """Deletes a page in HubSpot by ID."""
        endpoint = f"/cms/v3/pages/{page_id}"
        return self._make_request("DELETE", endpoint)

    def get_page(self, page_id: int):
        """Retrieves a page from HubSpot by ID."""
        endpoint = f"/cms/v3/pages/{page_id}"
        return self._make_request("GET", endpoint)

    def list_pages(self, limit=100, offset=0):
        """Lists pages from HubSpot with pagination support."""
        endpoint = "/cms/v3/pages"
        params = {
            "limit": limit,
            "offset": offset,
        }
        return self._make_request("GET", endpoint, params=params)
