from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
HTML_FILE = BASE_DIR / "data" / "nxp.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find tables that look like an income statement (Consolidated Statements of Operations)
# These typically contain: Revenue, Cost of revenue, Gross profit, Operating income
target_table = None
for table in soup.find_all("table"):
    table_text = table.get_text()
    # Look for key income statement line items
    has_revenue = "Revenue" in table_text
    has_cost = "Cost of revenue" in table_text
    has_operating = "Operating income" in table_text or "Operating expenses" in table_text
    has_net_income = "Net income" in table_text

    # This is likely our income statement table
    if has_revenue and has_cost and has_operating and has_net_income:
        target_table = table
        break

if not target_table:
    print("Table 'Consolidated Statements of Operations' not found")
else:
    opex = {}
    for row in target_table.find_all("tr"):
        cols = row.find_all(["td", "th"])
        if len(cols) >= 2:
            name = cols[0].get_text(strip=True)
            values = [col.get_text(strip=True) for col in cols[1:]]
            values = [v for v in values if v]
            if name and values:
                opex[name] = values

    print(opex)



