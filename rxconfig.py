import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="mySite",
    db_url="sqlite:///resume.db",
    plugins=[SitemapPlugin()],
)