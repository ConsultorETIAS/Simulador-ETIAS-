import os, glob
from datetime import date

BASE_URL = "https://consultoretias.github.io/Simulador-ETIAS-/"
REPO_DIR = os.path.expanduser("~/ETIAS-simulador")
HOY = date.today().isoformat()

htmls = sorted(glob.glob(os.path.join(REPO_DIR, "*.html")))

urls = []
for f in htmls:
    nombre = os.path.basename(f)
    if nombre.startswith("google"):
        continue
    prioridad = "1.0" if nombre == "index.html" else "0.7"
    urls.append(f"""  <url>
    <loc>{BASE_URL}{nombre}</loc>
    <lastmod>{HOY}</lastmod>
    <priority>{prioridad}</priority>
  </url>""")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

out = os.path.join(REPO_DIR, "sitemap.xml")
with open(out, "w") as f:
    f.write(sitemap)

print(f"✅ sitemap.xml generado con {len(urls)} URLs")
