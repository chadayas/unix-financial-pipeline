from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
HTML_FILE = BASE_DIR / "data" / "nxp.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

target_table = None
for table in soup.find_all("table"):
    table_text = table.get_text()
    # Look for key income statement line items
    has_revenue = "Revenue" in table_text
    has_cost = "Cost of revenue" in table_text
    has_operating = "Operating income" in table_text or "Operating expenses" in table_text
    has_net_income = "Net income" in table_text

    if has_revenue and has_cost and has_operating and has_net_income:
        target_table = table
        break

if not target_table:
    print("Table 'Consolidated Statements of Operations' not found")
else:
    all_data = {}
    for row in target_table.find_all("tr"):
        cols = row.find_all(["td", "th"])
        if len(cols) >= 2:
            name = cols[0].get_text(strip=True)
            values = [col.get_text(strip=True) for col in cols[1:]]
            values = [v for v in values if v]
            if name and values:
                all_data[name] = values

    expense_items = [
        "Research and development",
        "Selling, general and administrative",
        "Amortization of acquisition-related intangible assets",
    ]

    opex = {}
    for item in expense_items:
        if item in all_data:
            val = all_data[item][0]  # Most recent year
            val = val.replace(",", "").replace("(", "").replace(")", "")
            opex[item] = int(val)

abr_items = ["R&D", "SGA", "Amortization"] # Shorten items and get rid of whitespace.
for i in range(len(abr_items)):
    opex[abr_items[i]] = opex[expense_items[i]]
    del opex[expense_items[i]]

for k, v in opex.items():
    print(k , v)
