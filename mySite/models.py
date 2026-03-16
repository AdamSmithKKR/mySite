import reflex as rx
from typing import Optional

class ThemeConfig(rx.Model, table=True):
    """Stores the dynamic styling configuration."""
    name: str = "default"  # To query the config easily
    font_family: str
    base_font_size: str
    
    # Light Theme Colors
    light_bg: str
    light_accent: str
    light_text: str
    light_card_bg: str
    
    # Dark Theme Colors
    dark_bg: str
    dark_accent: str
    dark_text: str
    dark_card_bg: str
    
class Profile(rx.Model, table=True):
    name: str
    linkedin_url: str
    
    objective_title: str
    objective_text: str
    
    professional_summary_title: str
    professional_summary_text: str
    
    technical_summary_title: str
    technical_summary_text: str

class Education(rx.Model, table=True):
    year: str
    examination: str
    board_university: str
    order_index: int = 0

class Certification(rx.Model, table=True):
    name: str
    credential_info: str
    order_index: int = 0

class Skill(rx.Model, table=True):
    category: str # e.g., "language", "technical"
    name: str
    order_index: int = 0

class Company(rx.Model, table=True):
    name: str
    duration: str
    roles_and_responsibilities: str
    order_index: int = 0

class Project(rx.Model, table=True):
    company_id: int
    name: str
    customer: str
    technology_used: str
    description: str
    order_index: int = 0
