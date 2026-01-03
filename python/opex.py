from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
HTML_FILE = BASE_DIR / "data" / "nxp.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

opex = {}

# Example: table rows
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) != 2:
        continue

    name = cols[0].get_text(strip=True)
    value = cols[1].get_text(strip=True)

    # Remove commas, dollar signs, etc.
    value = value.replace(",", "").replace("$", "")
    if value.isdigit():
        opex[name] = int(value)

# Emit to stdout (pipeline-safe)
for name, amount in opex.items():
    print(name, amount)



