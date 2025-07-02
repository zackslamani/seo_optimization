import os
from datetime import datetime
from xml.sax.saxutils import escape

# --- Configuration ---
SITE_URL = "https://zackslamani.github.io/seo_optimization/"
ARTICLES_DIR = "articles"
OUTPUT_FILE = "rss.xml"

# --- Préparation des articles ---
articles = sorted(
    [f for f in os.listdir(ARTICLES_DIR) if f.endswith(".md")],
    key=lambda x: os.path.getmtime(os.path.join(ARTICLES_DIR, x)),
    reverse=True
)

# --- Génération des <item> ---
items = ""
for filename in articles:
    filepath = os.path.join(ARTICLES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    title = filename.replace("_", " ").replace(".md", "")
    link = f"{SITE_URL}articles/{filename.replace(' ', '%20')}"
    pub_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")

    items += f"""
  <item>
    <title>{escape(title)}</title>
    <link>{link}</link>
    <guid>{link}</guid>
    <pubDate>{pub_date}</pubDate>
    <description><![CDATA[{content[:1000]}...]]></description>
  </item>
"""

# --- Génération du flux RSS ---
rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>Articles Pinterest SEO</title>
  <link>{SITE_URL}</link>
  <description>Articles générés automatiquement à partir de questions sur Pinterest</description>
  <language>fr-fr</language>
  <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>
  <generator>Python Script</generator>
  {items}
</channel>
</rss>
"""

# --- Écriture ---
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(rss)

print("✅ rss.xml généré avec succès.")
