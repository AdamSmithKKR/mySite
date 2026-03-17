import reflex as rx
from ..state_config import AppState


def _nav_link(label: str, href: str, icon_tag: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon_tag, size=16),
            rx.text(label, font_size="0.9rem", font_weight="500"),
            spacing="2",
            align_items="center",
        ),
        href=href,
        text_decoration="none",
        color=rx.color_mode_cond(AppState.theme.light_text, AppState.theme.dark_text),
        padding="0.5rem 1rem",
        border_radius="12px",
        _hover={
            "background": rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.15)"),
            "transform": "translateY(-1px)",
        },
        transition="all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
    )


def header_component() -> rx.Component:

    logo_src = rx.color_mode_cond(
        light="/ktt_logo_black.png",
        dark="/KTT_logo_white.png",
    )

    return rx.box(
        rx.hstack(
            # Logo
            rx.image(
                src=logo_src,
                height="36px",
                cursor="pointer",
                _hover={"opacity": 0.8, "transform": "scale(1.05)"},
                transition="all 0.3s ease",
            ),
            # Navigation links
            rx.hstack(
                _nav_link("Home", "/", "home"),
                _nav_link("Services", "/services", "layers"),
                spacing="2",
                display="flex",
            ),
            rx.spacer(),
            # Right side actions
            rx.hstack(
                # LinkedIn icon
                rx.link(
                    rx.box(
                        rx.icon(tag="linkedin", size=20),
                        padding="0.5rem",
                        border_radius="50%",
                        background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                        color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                        cursor="pointer",
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
                # Mail icon
                rx.link(
                    rx.box(
                        rx.icon(tag="mail", size=20),
                        padding="0.5rem",
                        border_radius="50%",
                        background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                        color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                        cursor="pointer",
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
                # Theme toggle
                rx.box(
                    rx.icon(
                        tag=rx.color_mode_cond(light="moon", dark="sun"),
                        color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                        size=20,
                    ),
                    cursor="pointer",
                    on_click=rx.toggle_color_mode,
                    padding="0.5rem",
                    border_radius="50%",
                    background=rx.color_mode_cond("rgba(62,207,142,0.1)", "rgba(83,232,164,0.1)"),
                    _hover={
                        "transform": "rotate(180deg) scale(1.1)",
                        "background": rx.color_mode_cond("rgba(62,207,142,0.2)", "rgba(83,232,164,0.2)"),
                    },
                    transition="all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
                ),
                # Export PDF button
                rx.button(
                    rx.hstack(
                        rx.icon(tag="download", size=16),
                        rx.text("Export CV"),
                        spacing="2",
                        align_items="center",
                    ),
                    on_click=rx.call_script("window.print()"),
                    background=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                    color=rx.color_mode_cond("#FFFFFF", "#0A0F0D"),
                    border_radius="12px",
                    padding="0.5rem 1.2rem",
                    font_weight="600",
                    font_size="0.85rem",
                    border="none",
                    cursor="pointer",
                    _hover={
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 8px 25px -5px rgba(62,207,142,0.4)",
                    },
                    transition="all 0.3s cubic-bezier(0.16, 1, 0.3, 1)",
                ),
                spacing="4",
                align_items="center",
            ),
            width="100%",
            align_items="center",
        ),
        # Header container styling
        position="fixed",
        top="16px",
        left="50%",
        transform="translateX(-50%)",
        width="92%",
        max_width="1200px",
        z_index="1000",
        padding="0.8rem 1.5rem",
        class_name=rx.color_mode_cond(light="glass-panel-light no-print", dark="glass-panel-dark no-print"),
        transition="all 0.3s ease",
    )
