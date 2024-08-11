"""Contains class Contact."""

from dataclasses import dataclass


@dataclass
class Contact:
    """A simple data model for a contact."""
    first_name: str
    last_name: str
    email: str
