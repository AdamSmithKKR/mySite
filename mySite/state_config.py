from sqlmodel import select
import reflex as rx
from .models import ThemeConfig, Profile, Education, Certification, Skill, Company, Project

class AppState(rx.State):
    """The app state."""

    theme: ThemeConfig = ThemeConfig(
        name="default",
        font_family="Inter, sans-serif",
        base_font_size="16px",
        light_bg="#F5F7F5",  # Soft natural off-white
        light_accent="#3ECF8E", # Cute green
        light_text="#2B3A31",
        light_card_bg="rgba(255, 255, 255, 0.65)",
        dark_bg="#0F1712", # Deep charcoal green
        dark_accent="#53E8A4", 
        dark_text="#E8F1EC",
        dark_card_bg="rgba(25, 33, 28, 0.4)",
    )
    
    profile: Profile = Profile(
        name="Kirthik Raj",
        linkedin_url="https://www.linkedin.com/in/kirthik-raj-93952674",
        gmail_url="kirthikraj555@gmail.com",
        objective_title="Objective / Overview",
        objective_text="",
        professional_summary_title="Professional Summary",
        professional_summary_text="",
        technical_summary_title="Technical Experience Summary",
        technical_summary_text=""
    )
    
    education_list: list[Education] = []
    certifications: list[Certification] = []
    technical_skills: list[Skill] = []
    language_skills: list[Skill] = []
    companies: list[Company] = []
    projects: list[Project] = []

    active_tab: str = "Objective"
    active_company_id: int = -1
    show_company_list: bool = True

    def set_active_tab(self, tab: str):
        self.active_tab = tab

    def set_active_company(self, company_id: int):
        self.active_company_id = company_id

    def toggle_company_list(self):
        self.show_company_list = not self.show_company_list

    def toggle_companies_section(self):
        """Toggle the Companies section open/closed and activate the tab."""
        self.show_company_list = not self.show_company_list
        self.active_tab = "Companies / Experience"

    def select_company(self, company_id: int):
        """Select a company and switch to Companies / Experience tab."""
        self.active_company_id = company_id
        self.active_tab = "Companies / Experience"

    def load_data(self):
        """Load data from database into state"""
        from .seed import seed_db
        seed_db()
        
        with rx.session() as session:
            # Try to grab Theme Config
            db_theme = session.exec(select(ThemeConfig)).first()
            if db_theme:
                self.theme = db_theme

            # Profile
            db_prof = session.exec(select(Profile)).first()
            if db_prof:
                # Make sure we always have a valid email to render as a mailto: link
                if not db_prof.gmail_url:
                    db_prof.gmail_url = "kirthikraj555@gmail.com"
                    session.add(db_prof)
                    session.commit()
                self.profile = db_prof

            self.education_list = session.exec(select(Education).order_by(Education.order_index)).all()
            self.certifications = session.exec(select(Certification).order_by(Certification.order_index)).all()
            
            skills = session.exec(select(Skill).order_by(Skill.order_index)).all()
            self.technical_skills = [s for s in skills if s.category == 'technical']
            self.language_skills = [s for s in skills if s.category == 'language']
            
            self.companies = session.exec(select(Company).order_by(Company.order_index)).all()
            self.projects = session.exec(select(Project).order_by(Project.order_index)).all()
            
            if self.companies and self.active_company_id == -1:
                self.active_company_id = self.companies[0].id
