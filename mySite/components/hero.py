import reflex as rx
from ..state_config import AppState


# Lottie animation JSON URLs (from user-provided LottieFiles links)
LOTTIE_GROWING_PLANT = "https://lottie.host/f5478e35-2201-43e4-9041-f8be4c264fa9/bCXoOGoJjV.json"
LOTTIE_DESK_PLANT = "https://lottie.host/29563399-4945-4b21-bcb0-318ab0e125c2/4k3u4GQhEu.json"
LOTTIE_PLANT_3 = "https://lottie.host/80d3ab51-cded-4797-9948-d60a1fc44835/5CRKwCNElh.json"
LOTTIE_PLANT_4 = "https://lottie.host/4b453e62-9e3e-42ec-812c-fa7e8a5c42f5/HcWGmz4xg3.json"


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
            function updateVids() {
                var isDark = document.documentElement.classList.contains('dark');
                var vl = document.getElementById('hero-video-light');
                var vd = document.getElementById('hero-video-dark');
                if (vl && vd) {
                    vl.style.display = isDark ? 'none' : 'block';
                    vd.style.display = isDark ? 'block' : 'none';
                }
            }
            updateVids();
            var obs = new MutationObserver(updateVids);
            obs.observe(document.documentElement, {attributes: true, attributeFilter: ['class']});
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

        # ── Lottie Animations BEHIND the overlay (z-index:0) ──
        rx.html(f'''
        <div style="position:absolute;bottom:20px;right:5%;z-index:0;opacity:0.4;pointer-events:none;">
            <lottie-player src="{LOTTIE_GROWING_PLANT}" background="transparent" speed="0.8"
                style="width:280px;height:280px;" loop autoplay></lottie-player>
        </div>
        '''),
        rx.html(f'''
        <div style="position:absolute;bottom:60px;left:3%;z-index:0;opacity:0.3;pointer-events:none;">
            <lottie-player src="{LOTTIE_DESK_PLANT}" background="transparent" speed="0.6"
                style="width:220px;height:220px;" loop autoplay></lottie-player>
        </div>
        '''),
        rx.html(f'''
        <div style="position:absolute;top:15%;right:12%;z-index:0;opacity:0.25;pointer-events:none;">
            <lottie-player src="{LOTTIE_PLANT_3}" background="transparent" speed="0.5"
                style="width:180px;height:180px;" loop autoplay></lottie-player>
        </div>
        '''),

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
                rx.text(
                    AppState.profile.objective_text,
                    font_size="1.05rem",
                    max_width="650px",
                    line_height="1.7",
                    opacity="0.75",
                    margin_top="1.5rem",
                    class_name="animate-fade-in-up delay-3",
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
        height="75vh",
        width="100%",
        position="relative",
        overflow="hidden",
        class_name="hero-section no-print",
    )
