import os
import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="mySite",
    # Use DATABASE_URL env var on Reflex Cloud (set it to a Postgres/MySQL URL).
    # Falls back to local SQLite for development.
    db_url=os.environ.get("DATABASE_URL", "sqlite:///resume.db"),
    plugins=[SitemapPlugin()],
)