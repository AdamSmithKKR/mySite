import reflex as rx
from ..state_config import AppState


# ─── Content Renderers ───

def _render_objective_content() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="target", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading(AppState.profile.objective_title, size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.text(
            AppState.profile.objective_text,
            font_size="1.08rem",
            line_height="1.8",
            opacity="0.9",
        ),
        width="100%",
        spacing="5",
        class_name="animate-fade-in-up",
    )


def _render_professional_summary() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="briefcase", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading(AppState.profile.professional_summary_title, size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.foreach(
            AppState.profile.professional_summary_text.split("\n"),
            lambda line: rx.hstack(
                rx.icon(tag="chevron-right", size=16, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent), flex_shrink="0"),
                rx.text(line, font_size="1.02rem", line_height="1.7"),
                spacing="3",
                align_items="flex-start",
                padding="0.6rem 0",
            ),
        ),
        width="100%",
        spacing="3",
        class_name="animate-fade-in-up",
    )


def _render_technical_summary() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="wrench", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading(AppState.profile.technical_summary_title, size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.flex(
            rx.foreach(
                AppState.profile.technical_summary_text.split("\n"),
                lambda line: rx.box(
                    rx.hstack(
                        rx.icon(tag="zap", size=16, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent), flex_shrink="0", margin_top="2px"),
                        rx.text(line, font_size="0.95rem", line_height="1.6"),
                        spacing="3",
                        align_items="flex-start",
                    ),
                    padding="1.1rem 1.3rem",
                    class_name=rx.color_mode_cond("glass-card-light", "glass-card-dark"),
                    width="100%",
                    margin_bottom="0.75rem",
                ),
            ),
            direction="column",
            width="100%",
        ),
        width="100%",
        spacing="5",
        class_name="animate-fade-in-up",
    )


def _render_companies_section() -> rx.Component:
    """Render the collapsible Companies / Experience section in the left pane."""
    return rx.vstack(
        # Collapsible Header (acts as the section title)
        rx.box(
            rx.hstack(
                rx.icon(
                    tag=rx.cond(AppState.show_company_list, "chevron-down", "chevron-right"),
                    size=20,
                    color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                ),
                rx.text(
                    "Companies / Experience",
                    font_weight="600",
                    font_size="0.95rem",
                ),
                spacing="2",
                align_items="center",
                width="100%",
            ),
            padding="1rem 1.2rem",
            cursor="pointer",
            border_radius="12px",
            background=rx.cond(
                AppState.show_company_list,
                rx.color_mode_cond("rgba(62,207,142,0.08)", "rgba(83,232,164,0.08)"),
                "transparent",
            ),
            border=rx.cond(
                AppState.show_company_list,
                rx.color_mode_cond("1px solid rgba(62,207,142,0.2)", "1px solid rgba(83,232,164,0.15)"),
                "1px solid transparent",
            ),
            on_click=AppState.toggle_companies_section,
            _hover={"background": rx.color_mode_cond("rgba(62,207,142,0.12)", "rgba(83,232,164,0.12)")},
            transition="all 0.25s ease",
            margin_bottom="0.5rem",
        ),
        # Company Items (Collapsible Content)
        rx.cond(
            AppState.show_company_list,
            rx.vstack(
                rx.foreach(
                    AppState.companies,
                    lambda comp: rx.box(
                        rx.hstack(
                            rx.box(
                                rx.icon(tag="building-2", size=16, color=rx.cond(AppState.active_company_id == comp.id, rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent), "gray")),
                                padding="0.4rem",
                                border_radius="8px",
                                background=rx.cond(AppState.active_company_id == comp.id, rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"), "transparent"),
                            ),
                            rx.vstack(
                                rx.text(comp.name, font_weight="600", font_size="0.9rem"),
                                rx.text(comp.duration, font_size="0.75rem", color="gray"),
                                spacing="1",
                            ),
                            spacing="3",
                            align_items="center",
                        ),
                        padding="0.8rem 1rem",
                        width="100%",
                        cursor="pointer",
                        border_radius="12px",
                        background=rx.cond(
                            AppState.active_company_id == comp.id,
                            rx.color_mode_cond("rgba(62,207,142,0.08)", "rgba(83,232,164,0.08)"),
                            "transparent",
                        ),
                        border=rx.cond(
                            AppState.active_company_id == comp.id,
                            rx.color_mode_cond("1px solid rgba(62,207,142,0.2)", "1px solid rgba(83,232,164,0.15)"),
                            "1px solid transparent",
                        ),
                        on_click=AppState.select_company(comp.id),
                        _hover={"background": rx.color_mode_cond("rgba(0,0,0,0.02)", "rgba(255,255,255,0.02)")},
                        transition="all 0.25s ease",
                        margin_bottom="0.3rem",
                    ),
                ),
                width="100%",
                align_items="flex-start",
                spacing="0",
            ),
            rx.fragment(),
        ),
        width="100%",
        align_items="flex-start",
    )


def _render_companies() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="building", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading("Professional Experience", size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.foreach(
            AppState.companies,
            lambda comp: rx.cond(
                AppState.active_company_id == comp.id,
                rx.vstack(
                    rx.heading(comp.name, size="5", font_weight="700"),
                    rx.badge(comp.duration, color_scheme="green", variant="soft", font_size="0.8rem"),
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="clipboard-list", size=18, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                            rx.text("Roles & Responsibilities", font_weight="600", font_size="0.95rem"),
                            spacing="2",
                            align_items="center",
                        ),
                        rx.text(comp.roles_and_responsibilities, white_space="pre-wrap", font_size="0.93rem", line_height="1.7", opacity="0.85", margin_top="0.5rem"),
                        padding="1.2rem",
                        class_name=rx.color_mode_cond("glass-card-light", "glass-card-dark"),
                        width="100%",
                        margin_top="1rem",
                    ),
                    rx.hstack(
                        rx.icon(tag="folder-open", size=18, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                        rx.heading("Key Projects", size="4", font_weight="600"),
                        spacing="2",
                        align_items="center",
                        margin_top="1.5rem",
                    ),
                    rx.foreach(
                        AppState.projects,
                        lambda proj: rx.cond(
                            proj.company_id == comp.id,
                            rx.box(
                                rx.hstack(
                                    rx.icon(tag="folder-kanban", size=16, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                                    rx.text(proj.name, font_weight="600", font_size="1rem"),
                                    spacing="2",
                                    align_items="center",
                                ),
                                rx.hstack(
                                    rx.icon(tag="users", size=14, color="gray"),
                                    rx.text(proj.customer, font_size="0.85rem", font_style="italic", color="gray"),
                                    spacing="2",
                                    align_items="center",
                                    margin_top="0.5rem",
                                ),
                                rx.hstack(
                                    rx.icon(tag="cpu", size=14, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                                    rx.text(proj.technology_used, font_size="0.85rem", font_weight="500"),
                                    spacing="2",
                                    align_items="center",
                                    margin_top="0.3rem",
                                ),
                                rx.text(proj.description, font_size="0.93rem", line_height="1.6", opacity="0.85", margin_top="0.6rem"),
                                padding="1.2rem",
                                class_name=rx.color_mode_cond("glass-card-light", "glass-card-dark"),
                                margin_bottom="0.75rem",
                            ),
                            rx.fragment(),
                        ),
                    ),
                    width="100%",
                    padding_left="2rem",
                    class_name="animate-fade-in-up",
                ),
                rx.fragment(),
            ),
        ),
        width="100%",
        spacing="5",
        class_name="animate-fade-in-up",
    )

def _render_education() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="graduation-cap", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading("Education", size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.foreach(
            AppState.education_list,
            lambda edu: rx.box(
                rx.hstack(
                    rx.badge(edu.year, color_scheme="green", variant="soft", font_size="0.8rem"),
                    rx.vstack(
                        rx.text(edu.examination, font_weight="600", font_size="0.95rem"),
                        rx.text(edu.board_university, font_size="0.85rem", color="gray"),
                        spacing="1",
                    ),
                    spacing="4",
                    align_items="center",
                ),
                padding="1rem 1.2rem",
                class_name=rx.color_mode_cond("glass-card-light", "glass-card-dark"),
                width="100%",
                margin_bottom="0.6rem",
            ),
        ),
        width="100%",
        spacing="4",
        class_name="animate-fade-in-up",
    )


def _render_certifications() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="award", size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading("Certifications", size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.foreach(
            AppState.certifications,
            lambda cert: rx.box(
                rx.hstack(
                    rx.box(
                        rx.icon(tag="shield-check", size=20, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                        padding="0.5rem",
                        border_radius="10px",
                        background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                    ),
                    rx.vstack(
                        rx.text(cert.name, font_weight="600", font_size="0.95rem"),
                        rx.cond(
                            cert.credential_info != "",
                            rx.cond(
                                cert.credential_info.contains("http"),
                                rx.link(
                                    rx.hstack(
                                        rx.icon(tag="external-link", size=14),
                                        rx.text("View Credential"),
                                        spacing="2",
                                        align_items="center",
                                    ),
                                    href=cert.credential_info,
                                    is_external=True,
                                    color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                                    font_size="0.85rem",
                                    _hover={"opacity": "0.8"},
                                ),
                                rx.text(cert.credential_info, font_size="0.82rem", color="gray"),
                            ),
                            rx.fragment(),
                        ),
                        spacing="1",
                    ),
                    spacing="4",
                    align_items="center",
                ),
                padding="1rem 1.2rem",
                class_name=rx.color_mode_cond("glass-card-light", "glass-card-dark"),
                width="100%",
                margin_bottom="0.6rem",
            ),
        ),
        width="100%",
        spacing="4",
        class_name="animate-fade-in-up",
    )


def _render_skills(title: str, icon_tag: str, items) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag=icon_tag, size=24, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
            rx.heading(title, size="6", font_weight="700"),
            spacing="3",
            align_items="center",
            class_name="section-accent",
        ),
        rx.flex(
            rx.foreach(
                items,
                lambda skill: rx.box(
                    rx.hstack(
                        rx.icon(tag="circle-check", size=14, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                        rx.text(skill.name, font_size="0.88rem", font_weight="500"),
                        spacing="2",
                        align_items="center",
                    ),
                    padding="0.45rem 1rem",
                    border_radius="50px",
                    background=rx.color_mode_cond("rgba(62,207,142,0.08)", "rgba(83,232,164,0.08)"),
                    border=rx.color_mode_cond("1px solid rgba(62,207,142,0.15)", "1px solid rgba(83,232,164,0.12)"),
                    class_name="skill-badge",
                    margin="0.3rem",
                ),
            ),
            wrap="wrap",
            width="100%",
        ),
        width="100%",
        spacing="4",
        class_name="animate-fade-in-up",
    )


# ═══════════════════════════════════════════
# Card-Based Layout View
# ═══════════════════════════════════════════
def card_layout_view() -> rx.Component:
    """
    Sections rendered as distinct cards:
      1. Objective        – full-width, overlaps hero
      2. Prof Summary + Tech Summary  – side by side
      3. Companies / Experience       – existing split-pane intact
      4. Tech Skills + Linguistic     – side by side
      5. Education + Certifications   – side by side
    """
    _card_shadow = rx.color_mode_cond(
        "0 8px 32px rgba(0,0,0,0.08), 0 2px 8px rgba(62,207,142,0.05)",
        "0 8px 32px rgba(0,0,0,0.3), 0 2px 8px rgba(83,232,164,0.04)",
    )
    _hero_card_shadow = rx.color_mode_cond(
        "0 20px 60px rgba(0,0,0,0.08), 0 4px 15px rgba(62,207,142,0.06)",
        "0 20px 60px rgba(0,0,0,0.3), 0 4px 15px rgba(83,232,164,0.05)",
    )

    return rx.vstack(

        # ── 1. Objective: full-width card (overlaps hero) ──────────────────
        rx.box(
            _render_objective_content(),
            padding="2.5rem 3rem",
            border_radius="24px",
            width="100%",
            class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
            box_shadow=_hero_card_shadow,
        ),

        # ── 2. Professional Summary  |  Technical Summary ──────────────────
        rx.box(
            rx.box(
                _render_professional_summary(),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            rx.box(
                _render_technical_summary(),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            class_name="side-by-side-row",
        ),

        # ── 3. Companies / Experience (split-pane layout preserved) ─────────
        rx.box(
            rx.flex(
                # Left: collapsible company navigator
                rx.vstack(
                    rx.hstack(
                        rx.icon(
                            tag="building-2",
                            size=20,
                            color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                        ),
                        rx.text(
                            "Experience",
                            font_weight="700",
                            font_size="0.85rem",
                            text_transform="uppercase",
                            letter_spacing="0.08em",
                        ),
                        spacing="2",
                        align_items="center",
                        padding="0.5rem 1.2rem",
                        margin_bottom="0.5rem",
                        opacity="0.7",
                    ),
                    _render_companies_section(),
                    width="280px",
                    min_width="280px",
                    padding="1.5rem 1rem",
                    align_items="flex-start",
                    border_right=rx.color_mode_cond(
                        "1px solid rgba(62,207,142,0.1)",
                        "1px solid rgba(83,232,164,0.08)",
                    ),
                    min_height="500px",
                    class_name="resume-left",
                ),
                # Right: company details
                rx.box(
                    _render_companies(),
                    flex="1",
                    padding="3rem",
                    class_name="resume-right",
                    overflow_y="auto",
                ),
                direction="row",
                width="100%",
                align_items="stretch",
                class_name="resume-layout",
            ),
            width="100%",
            border_radius="24px",
            overflow="hidden",
            class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
            box_shadow=_hero_card_shadow,
        ),

        # ── 4. Technical Skills  |  Linguistic Ability ─────────────────────
        rx.box(
            rx.box(
                _render_skills("Technical Skills", "code", AppState.technical_skills),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            rx.box(
                _render_skills("Linguistic Ability", "languages", AppState.language_skills),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            class_name="side-by-side-row",
        ),

        # ── 5. Education  |  Certifications ───────────────────────────────
        rx.box(
            rx.box(
                _render_education(),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            rx.box(
                _render_certifications(),
                padding="2.5rem",
                border_radius="20px",
                class_name=rx.color_mode_cond("glass-panel-light", "glass-panel-dark"),
                box_shadow=_card_shadow,
            ),
            class_name="side-by-side-row",
        ),

        width="100%",
        spacing="5",
        align_items="stretch",
        margin_top="-12vh",
        position="relative",
        z_index="20",
    )
