import reflex as rx
from ..state_config import AppState


def hero_section() -> rx.Component:
    return rx.box(
        # ── Background Video (Light mode) ──
        rx.html(
            """
            <video id="hero-video-light" autoplay muted loop playsinline
                   style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:0;">
                <source src="/Green_plants_waving_in_wind_White.mp4" type="video/mp4"/>
            </video>
            """,
        ),
        # ── Background Video (Dark mode) ──
        rx.html(
            """
            <video id="hero-video-dark" autoplay muted loop playsinline
                   style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:0;display:none;">
                <source src="/Green_plants_waving_in_Dark.mp4" type="video/mp4"/>
            </video>
            """,
        ),

        # ── Script to toggle videos based on theme ──
        rx.html("""
        <script>
        (function() {
            function isDarkMode() {
                const styleScheme = document.documentElement.style.colorScheme;
                if (styleScheme) return styleScheme === "dark";
                return document.documentElement.classList.contains('dark');
            }

            function updateVids() {
                var isDark = isDarkMode();
                var vl = document.getElementById('hero-video-light');
                var vd = document.getElementById('hero-video-dark');
                if (vl && vd) {
                    vl.style.display = isDark ? 'none' : 'block';
                    vd.style.display = isDark ? 'block' : 'none';
                }
            }
            updateVids();
            var obs = new MutationObserver(updateVids);
            obs.observe(document.documentElement, {attributes: true, attributeFilter: ['class', 'style']});
        })();
        </script>
        """),

        # ── Translucent gradient overlay that fades into page ──
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            z_index="1",
            background=rx.color_mode_cond(
                light="linear-gradient(to bottom, rgba(245,247,245,0.45) 0%, rgba(245,247,245,0.7) 35%, rgba(245,247,245,0.92) 65%, #F5F7F5 100%)",
                dark="linear-gradient(to bottom, rgba(15,23,18,0.45) 0%, rgba(15,23,18,0.75) 35%, rgba(15,23,18,0.95) 65%, #0F1712 100%)",
            ),
        ),

        # ── Foreground Hero Content ──
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="leaf", size=28, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                    rx.text(
                        "Hello, I'm",
                        font_size="1.3rem",
                        font_weight="500",
                        color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent),
                    ),
                    spacing="3",
                    align_items="center",
                    class_name="animate-fade-in-up",
                ),
                rx.heading(
                    AppState.profile.name,
                    font_size="4.5rem",
                    font_weight="800",
                    letter_spacing="-0.04em",
                    line_height="1.1",
                    class_name="animate-fade-in-up delay-1",
                    color=rx.color_mode_cond(AppState.theme.light_text, AppState.theme.dark_text),
                    style={"font_family": "'Space Grotesk', 'Inter', sans-serif"},
                ),
                rx.hstack(
                    rx.icon(tag="briefcase", size=20, color=rx.color_mode_cond(AppState.theme.light_accent, AppState.theme.dark_accent)),
                    rx.text(
                        "Technology Architect  •  BPM Maestro  •  11+ Years",
                        font_size="1.25rem",
                        font_weight="400",
                        opacity="0.85",
                    ),
                    spacing="3",
                    align_items="center",
                    margin_top="1rem",
                    class_name="animate-fade-in-up delay-2",
                    color=rx.color_mode_cond(AppState.theme.light_text, AppState.theme.dark_text),
                ),
                spacing="3",
                align_items="flex-start",
                padding="0 8%",
                max_width="1200px",
                width="100%",
                margin="0 auto",
            ),
            width="100%",
            height="100%",
            justify_content="center",
            position="relative",
            z_index="5",
        ),

        # ── Hero container ──
        height="55vh",
        width="100%",
        position="relative",
        overflow="hidden",
        class_name="hero-section no-print",
    )
