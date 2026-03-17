import reflex as rx

from rxconfig import config
from .state_config import AppState
from . import models
from .components import header, hero, resume_view
from .components.print_cv import print_cv_view


# Local Lottie animation files (served from /assets)
LOTTIE_GROWING_PLANT = "/Growing Plant.lottie"
LOTTIE_DESK_PLANT = "/Plant, Office, Desk.lottie"
LOTTIE_PLANT_3 = "/Plants.lottie"
LOTTIE_PLANT_4 = "/Animated plant loader..lottie"


def index() -> rx.Component:
    return rx.box(
        # Load Lottie player script
        rx.script(src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"),

        # Floating header
        header.header_component(),

        # Main layout
        rx.vstack(
            hero.hero_section(),

            # ── Resume Cards area with Lottie decorations on sides ──
            rx.box(
                # Left Lottie decoration (beside cards)
                rx.html(f'''
                <div class="lottie-bg-left no-print" style="position:absolute;left:-100px;top:40%;z-index:0;opacity:0.15;pointer-events:none;">
                    <lottie-player src="{LOTTIE_PLANT_3}" background="transparent" speed="0.4"
                        style="width:200px;height:200px;" loop autoplay></lottie-player>
                </div>
                '''),
                # Right Lottie decoration (beside cards)
                rx.html(f'''
                <div class="lottie-bg-right no-print" style="position:absolute;right:-100px;top:25%;z-index:0;opacity:0.15;pointer-events:none;">
                    <lottie-player src="{LOTTIE_PLANT_4}" background="transparent" speed="0.5"
                        style="width:200px;height:200px;" loop autoplay></lottie-player>
                </div>
                '''),

                resume_view.split_pane_view(),
                width="100%",
                max_width="1200px",
                margin="0 auto",
                padding="2rem",
                z_index="10",
                position="relative",
                id="resume-content",
                overflow="visible",
            ),
            width="100%",
            spacing="0",
        ),

        # ── Sequential print-only CV (hidden on screen) ──
        print_cv_view(),

        # ── Footer with Lottie decorations ──
        rx.box(
            # Left footer Lottie
            rx.html(f'''
            <div class="footer-lottie" style="position:absolute;left:2%;bottom:0;opacity:0.18;pointer-events:none;z-index:0;">
                <lottie-player src="{LOTTIE_GROWING_PLANT}" background="transparent" speed="0.6"
                    style="width:160px;height:160px;" loop autoplay></lottie-player>
            </div>
            '''),
            # Right footer Lottie
            rx.html(f'''
            <div class="footer-lottie" style="position:absolute;right:2%;bottom:0;opacity:0.18;pointer-events:none;z-index:0;">
                <lottie-player src="{LOTTIE_DESK_PLANT}" background="transparent" speed="0.5"
                    style="width:160px;height:160px;" loop autoplay></lottie-player>
            </div>
            '''),

            rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="leaf", size=20, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                        rx.text(
                            "Kirthik Raj",
                            font_weight="700",
                            font_size="1.1rem",
                        ),
                        spacing="2",
                        align_items="center",
                    ),
                    rx.text(
                        "Technology Architect  •  BPM Maestro",
                        font_size="0.85rem",
                        opacity="0.6",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.box(
                                rx.icon(tag="linkedin", size=20),
                                padding="0.6rem",
                                border_radius="50%",
                                background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                                color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                                _hover={
                                    "transform": "translateY(-3px) scale(1.1)",
                                    "background": rx.color_mode_cond("rgba(62,207,142,0.2)", "rgba(83,232,164,0.2)"),
                                    "box_shadow": "0 6px 15px rgba(62,207,142,0.2)",
                                },
                                transition="all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
                            ),
                            href=AppState.profile.linkedin_url,
                            is_external=True,
                        ),
                        rx.link(
                            rx.box(
                                rx.icon(tag="mail", size=20),
                                padding="0.6rem",
                                border_radius="50%",
                                background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                                color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                                _hover={
                                    "transform": "translateY(-3px) scale(1.1)",
                                    "background": rx.color_mode_cond("rgba(62,207,142,0.2)", "rgba(83,232,164,0.2)"),
                                    "box_shadow": "0 6px 15px rgba(62,207,142,0.2)",
                                },
                                transition="all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
                            ),
                            href=f"mailto:{AppState.profile.gmail_url}",
                            is_external=True,
                        ),
                        spacing="3",
                        margin_top="0.5rem",
                    ),
                    rx.text(
                        "© 2025 Kirthik Raj. Crafted with 🌱",
                        font_size="0.75rem",
                        opacity="0.4",
                        margin_top="1rem",
                    ),
                    align_items="center",
                    spacing="2",
                    position="relative",
                    z_index="1",
                ),
            ),
            width="100%",
            padding="3rem 2rem",
            class_name="no-print",
            border_top=rx.color_mode_cond("1px solid rgba(62,207,142,0.1)", "1px solid rgba(83,232,164,0.08)"),
            position="relative",
            overflow="hidden",
        ),

        # Root container
        background=rx.color_mode_cond(AppState.theme.light_bg, AppState.theme.dark_bg),
        min_height="100vh",
        width="100%",
        font_family=AppState.theme.font_family,
        color=rx.color_mode_cond(AppState.theme.light_text, AppState.theme.dark_text),
        transition="background-color 0.4s ease, color 0.4s ease",
        overflow_x="hidden",
    )


def services() -> rx.Component:
    """Placeholder Services page – to be built later."""
    return rx.box(
        rx.script(src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"),
        header.header_component(),
        rx.center(
            rx.vstack(
                rx.icon(tag="construction", size=64, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                rx.heading("Services", size="8", font_weight="700"),
                rx.text("Coming soon — this page is under construction.", font_size="1.1rem", opacity="0.7"),
                spacing="5",
                align_items="center",
                padding_top="120px",
            ),
        ),
        background=rx.color_mode_cond(AppState.theme.light_bg, AppState.theme.dark_bg),
        min_height="100vh",
        font_family=AppState.theme.font_family,
        color=rx.color_mode_cond(AppState.theme.light_text, AppState.theme.dark_text),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="jade",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap",
        "/styles.css",
    ],
)

app.add_page(index, route="/", title="Kirthik Raj | Technology Architect", on_load=AppState.load_data)
app.add_page(services, route="/services", title="Services | Kirthik Raj")
