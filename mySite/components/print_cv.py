"""
Print-only component that renders ALL resume data sequentially
for the Export CV (window.print()) flow.
This is hidden on screen and only shown via @media print.
"""
import reflex as rx
from ..state_config import AppState


def print_cv_view() -> rx.Component:
    """A flat, sequential CV layout that is hidden on screen but shown when printing."""
    return rx.box(
        # ── Header ──
        rx.vstack(
            rx.heading(AppState.profile.name, size="8", font_weight="800"),
            rx.text(
                "Technology Architect  •  BPM Maestro  •  11+ Years",
                font_size="1rem", opacity="0.7",
            ),
            rx.hstack(
                rx.link(
                    rx.text("LinkedIn", font_weight="600"),
                    href=AppState.profile.linkedin_url,
                    is_external=True,
                    font_size="0.85rem",
                    color="#0A66C2",
                    text_decoration="underline",
                    display="inline",
                    target="_blank",
                ),
                rx.link(
                    rx.text("Email: " + AppState.profile.gmail_url, font_weight="600"),
                    href="mailto:" + AppState.profile.gmail_url,
                    font_size="0.85rem",
                    color="#EA4335",
                    text_decoration="underline",
                    display="inline",
                ),
                spacing="3",
                align_items="center",
            ),
            spacing="2",
            align_items="center",
            width="100%",
            padding_bottom="1rem",
            border_bottom="2px solid #3ECF8E",
            margin_bottom="1.5rem",
        ),

        # ── Objective ──
        rx.vstack(
            rx.heading(AppState.profile.objective_title, size="5", font_weight="700"),
            rx.text(AppState.profile.objective_text, font_size="0.95rem", line_height="1.6"),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Professional Summary ──
        rx.vstack(
            rx.heading(AppState.profile.professional_summary_title, size="5", font_weight="700"),
            rx.foreach(
                AppState.profile.professional_summary_text.split("\n"),
                lambda line: rx.text("• " + line, font_size="0.92rem", line_height="1.5", margin_bottom="0.3rem"),
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Technical Summary ──
        rx.vstack(
            rx.heading(AppState.profile.technical_summary_title, size="5", font_weight="700"),
            rx.foreach(
                AppState.profile.technical_summary_text.split("\n"),
                lambda line: rx.text("• " + line, font_size="0.92rem", line_height="1.5", margin_bottom="0.3rem"),
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Technical Skills ──
        rx.vstack(
            rx.heading("Technical Skills", size="5", font_weight="700"),
            rx.flex(
                rx.foreach(
                    AppState.technical_skills,
                    lambda s: rx.text(s.name, font_size="0.88rem", padding="0.2rem 0.6rem",
                                      border="1px solid #ddd", border_radius="4px", margin="0.2rem"),
                ),
                wrap="wrap", width="100%",
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Education ──
        rx.vstack(
            rx.heading("Education", size="5", font_weight="700"),
            rx.foreach(
                AppState.education_list,
                lambda edu: rx.hstack(
                    rx.text(edu.year, font_weight="600", min_width="50px"),
                    rx.text(" — ", opacity="0.5"),
                    rx.text(edu.examination, font_weight="500"),
                    rx.text(" — " + edu.board_university, font_size="0.85rem", color="gray"),
                    spacing="2", align_items="center", width="100%",
                ),
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Linguistic Ability ──
        rx.vstack(
            rx.heading("Linguistic Ability", size="5", font_weight="700"),
            rx.flex(
                rx.foreach(
                    AppState.language_skills,
                    lambda s: rx.text(s.name, font_size="0.88rem", padding="0.2rem 0.6rem",
                                      border="1px solid #ddd", border_radius="4px", margin="0.2rem"),
                ),
                wrap="wrap", width="100%",
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Certifications ──
        rx.vstack(
            rx.heading("Certifications", size="5", font_weight="700"),
            rx.foreach(
                AppState.certifications,
                lambda cert: rx.vstack(
                    rx.text(cert.name, font_weight="600", font_size="0.92rem"),
                    rx.cond(
                        cert.credential_info != "",
                        rx.cond(
                            cert.credential_info.contains("http"),
                            rx.link(
                                cert.credential_info,
                                href=cert.credential_info,
                                is_external=True,
                                target="_blank",
                                font_size="0.8rem",
                                color="#0A66C2",
                                text_decoration="underline",
                            ),
                            rx.text(cert.credential_info, font_size="0.8rem", color="gray"),
                        ),
                        rx.fragment(),
                    ),
                    spacing="1", width="100%", padding_bottom="0.5rem",
                    border_bottom="1px solid #eee", margin_bottom="0.5rem",
                ),
            ),
            spacing="2", width="100%", margin_bottom="1.5rem",
        ),

        # ── Professional Experience (ALL companies, ALL projects) ──
        rx.vstack(
            rx.heading("Professional Experience", size="5", font_weight="700"),
            rx.foreach(
                AppState.companies,
                lambda comp: rx.vstack(
                    rx.hstack(
                        rx.text(comp.name, font_weight="700", font_size="1rem"),
                        rx.spacer(),
                        rx.text(comp.duration, font_size="0.85rem", color="gray"),
                        width="100%", align_items="center",
                    ),
                    rx.text(comp.roles_and_responsibilities, white_space="pre-wrap",
                            font_size="0.88rem", line_height="1.5", opacity="0.85",
                            margin_top="0.3rem"),
                    # Projects under this company
                    rx.foreach(
                        AppState.projects,
                        lambda proj: rx.cond(
                            proj.company_id == comp.id,
                            rx.box(
                                rx.text(proj.name, font_weight="600", font_size="0.92rem"),
                                rx.text("Customer: " + proj.customer, font_size="0.82rem", color="gray"),
                                rx.text("Tech: " + proj.technology_used, font_size="0.82rem", font_weight="500"),
                                rx.text(proj.description, font_size="0.88rem", line_height="1.5", margin_top="0.3rem"),
                                padding="0.8rem",
                                border_left="3px solid #3ECF8E",
                                margin_top="0.5rem",
                                margin_bottom="0.5rem",
                                background="#fafafa",
                            ),
                            rx.fragment(),
                        ),
                    ),
                    width="100%",
                    padding_bottom="1rem",
                    border_bottom="1px solid #eee",
                    margin_bottom="1rem",
                ),
            ),
            spacing="2", width="100%",
        ),

        # Container — hidden on screen, shown on print
        width="100%",
        display="none",
        class_name="print-cv-section",
        padding="0.5rem",
    )
