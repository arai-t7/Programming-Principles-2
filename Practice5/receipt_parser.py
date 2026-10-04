import re
import json
from pathlib import Path

text = (Path(__file__).parent / "raw.txt").read_text(encoding="utf-8")

pattern = (
    r"(?m)^\s*\d+\.\s*$\n"
    r"\s*(.+?)\s*$\n"
    r"\s*([\d\s]+,\d{3})\s*x\s*([\d\s]+,\d{2})\s*$\n"
    r"\s*([\d\s]+,\d{2})\s*$"
)

matches = re.findall(pattern, text)

products = []

for name, quantity, unit_price, price in matches:
    products.append({
        "name": name.strip(),
        "quantity": float(quantity.replace(" ", "").replace(",", ".")),
        "unit_price": float(unit_price.replace(" ", "").replace(",", ".")),
        "price": float(price.replace(" ", "").replace(",", "."))
    })

total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)

total = (
    float(total_match.group(1).replace(" ", "").replace(",", "."))
    if total_match else None
)

datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
)

payment_match = re.search(
    r"(Банковская карта|Наличные)",
    text,
    re.IGNORECASE
)

result = {
    "products": products,
    "calculated_total": sum(product["price"] for product in products),
    "receipt_total": total,
    "date": datetime_match.group(1) if datetime_match else None,
    "time": datetime_match.group(2) if datetime_match else None,
    "payment_method": payment_match.group(1) if payment_match else None
}

print(json.dumps(result, ensure_ascii=False, indent=4))