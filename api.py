import requests
import logging
from .models import HubSpotPage, HubSpotPageUpdate

logger = logging.getLogger(__name__)

class HubSpotAPI:
    """Client for interacting with the HubSpot CMS API."""

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.hubapi.com"

    def _make_request(self, method, endpoint, params=None, data=None):
        """Handles API requests, error handling, and logging."""
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.request(method, url, params=params, json=data, headers=headers)
        try:
            response.raise_for_status()  # Raise for HTTP errors
        except requests.exceptions.HTTPError as err:
            error_details = response.json().get('message', '')
            logger.error(f"HTTP Error: {err}, Details: {error_details}")
            raise  # Re-raise the exception for the caller to handle (optional)
        except requests.exceptions.RequestException as err:
            logger.error(f"Request Exception: {err}")
            raise  # Re-raise the exception for the caller to handle (optional)

        return response.json()

    def create_page(self, page: HubSpotPage):
        """Creates a new page in HubSpot."""
        endpoint = "/cms/v3/pages"
        page.validate()  # Validate before sending
        data = page.to_dict()  # Convert to dictionary
        return self._make_request("POST", endpoint, data=data)

    def update_page(self, page_update: HubSpotPageUpdate):
        """Updates an existing page in HubSpot."""
        endpoint = f"/cms/v3/pages/{page_update.id}"
        page_update.validate()  
        data = page_update.to_dict()
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
