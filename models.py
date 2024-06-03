from dataclasses import dataclass, field
from typing import Optional
import re


@dataclass
class HubSpotPage:
    id: Optional[int] = field(default=None, compare=False)  # Compare=False for __eq__
    name: str = field(default="")
    slug: str = field(default="")
    meta_description: str = field(default="")
    html: str = field(default="")

    def __post_init__(self):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")

        self.validate()  # Auto-validate on creation

    def validate(self):
        """Validate page data, raising exceptions for invalid data."""
        if not self.validate_slug():
            raise ValueError(f"Invalid slug: {self.slug}. HubSpot slugs must be lowercase, hyphenated, and alphanumeric.")

    def validate_slug(self):
        """Validates the slug against HubSpot requirements."""
        # More concise regex (same logic)
        return bool(self.slug and re.match("^[a-z0-9]+(-[a-z0-9]+)*$", self.slug)) 

    def to_dict(self):
        """Convert page data to a dictionary for API requests."""
        return {
            "name": self.name,
            "html": self.html,
            "slug": self.slug,
            "meta_description": self.meta_description,
        }
  

@dataclass
class HubSpotPageUpdate:
    id: int
    name: Optional[str] = field(default=None, compare=False)  # Allow name updates
    html: Optional[str] = field(default=None, compare=False)  # Allow html updates
    meta_description: Optional[str] = field(default=None, compare=False)  # Allow description updates

    def validate(self):
        """Validate update data, only if name is changed."""
        if self.name is not None and not HubSpotPage.validate_slug(self):
            raise ValueError(f"Invalid new slug: {self.name}.")

    def to_dict(self):
        """Prepare update data dictionary for the API call."""
        update_data = {}
        if self.name is not None:
            update_data['name'] = self.name
        if self.html is not None:
            update_data['html'] = self.html
        if self.meta_description is not None:
            update_data['meta_description'] = self.meta_description
        return update_data
