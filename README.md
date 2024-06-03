# hs_utils: Your HubSpot CMS API Utility Toolkit

**[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)** 

`hs_utils` is a Python package designed to streamline interactions with the HubSpot CMS (Content Management System) API. It provides a convenient way to create, update, retrieve, and delete pages programmatically.

## Features

* **Page Management:**
   * Create new pages with custom content and metadata.
   * Update existing pages' content, title, or meta description.
   * Retrieve detailed information for specific pages.
   * List all pages in your HubSpot account with pagination support.
   * Delete pages efficiently.
* **Data Validation:**
   * Ensures data integrity by validating page slugs and other required fields.
   * Customizable validation rules can be added for your specific use cases.
* **Batch Operations (Optional):**
   * Perform bulk updates and deletes for improved efficiency (when available in the HubSpot API).
* **Robust Error Handling:**
   * Includes thorough error handling and logging to identify and diagnose issues.

## Installation

1. **Clone the Repository:**
   
2. Create a Virtual Environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies:

```
pip install -r requirements.txt
```

## Configuration
Create a Config File:
Copy the config/config.json.example file to config/config.json and fill in the following values:

```
{
    "wp_api_url": "[https://your-wordpress-site.com/wp-json/wp/v2/pages](https://your-wordpress-site.com/wp-json/wp/v2/pages)",
    "hubspot_api_url": "[https://api.hubapi.com/cms/v3/pages](https://api.hubapi.com/cms/v3/pages)",
    "hubspot_api_key": "YOUR_HUBSPOT_API_KEY",
    "batch_size": 50,  
    "db_url": "postgresql://user:password@localhost/your_database"  
}
```

Replace the placeholders with your actual WordPress site URL, HubSpot API key, and database connection string.

## Usage

```
from hs_utils.api import HubSpotAPI
from hs_utils.models import HubSpotPage

# Initialize API client
api = HubSpotAPI(api_key="YOUR_HUBSPOT_API_KEY")

# Create a new page
new_page = HubSpotPage(
    name="New Page Title", 
    html="<p>This is the page content.</p>", 
    meta_description="A brief description of the page."
)
api.create_page(new_page)
```

See the scripts directory for examples of how to use the package for different operations (migration, updating, etc.).
