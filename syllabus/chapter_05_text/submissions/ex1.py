feed = (
    "SKU-301|Blue Mug|12|4.99",
    "  sku-302 | Red Mug | 40 | 5.49 ",
    "SKU-303|Green Mug|abc|3.10",
    "SKU-304|Yellow Mug|7",
    "sku-305|Black Mug|0|8.00",
    "SKU-306|White Mug|5|12.75",
)
ACCEPTED = []
REJECTED = []
total_stock_value = 0.00

for line in feed:
    fields = line.strip().split("|")

    if len(fields) != 4:
        REJECTED.append((line.strip(), f"expected 4 fields, found {len(fields)}"))
        continue

    sku = fields[0].strip().upper()
    name = fields[1].strip()
    raw_qty = fields[2].strip()
    raw_price = fields[3].strip()

    if not raw_qty.isdigit():
        REJECTED.append((sku, "quantity is not a number"))
        continue

    if raw_price == "":
        REJECTED.append((sku, "price is missing"))
        continue

    qty = int(raw_qty)
    price = float(raw_price)

    if qty == 0:
        REJECTED.append((sku, "out of stock"))
        continue

    ACCEPTED.append((sku, name, qty, price))

print(f"ACCEPTED ({len(ACCEPTED)})")

if ACCEPTED:
    for sku, name, qty, price in ACCEPTED:
        line_value = qty * price
        print(f"  {sku:<10}{name:<12}{qty:>4}{price:>8.2f}{line_value:>10.2f}")
        total_stock_value += line_value
else:
    print("  none")

print(f"REJECTED ({len(REJECTED)})")
if REJECTED:
    for what, why in REJECTED:
        print(f"  {what:<28}{why}")
else:
    print("  none")

print("-" * 44)
print(f"{len(feed)} lines   {len(ACCEPTED)} accepted   {len(REJECTED)} rejected   value {total_stock_value:,.2f}")
