rows = (
    ("SKU-306", "White Mug", 5, 12.75),
    ("SKU-301", "Blue Mug", 12, 4.99),
    ("SKU-302", "Red Mug", 40, 5.49),
)

HEADERS = ("sku", "name", "qty", "price")
width_of_headers = []
width_of_items = []
headers = "|".join(HEADERS)

lines = sorted(rows)

ROWS = []
export = []
character_count = 0

for line in lines:
    parts = []
    for item in line:
        if type(item) == float:
            item = f"{item:.2f}"
        item = str(item)
        parts.append(item)
    new_parts = "|".join(parts)
    ROWS.append(new_parts)



print("EXPORT")
print(f"  {headers}")
character_count += len(headers)



for rows in ROWS:
    print(f"  {rows}")
    character_count += len(rows)

for index,item in enumerate(HEADERS):
    width_of_headers.append((index,item, len(item)))

for row in ROWS:
    new_row = row.split("|")
    for index,item in enumerate(new_row):
        width_of_items.append((index, len(item)))

combined = []

for header_index,header, header_length in width_of_headers:
    for item_index,item_length in width_of_items:
        if header_index == item_index:
            widest_length = max(header_length,item_length)
    combined.append((header, widest_length))



print("WIDTHS")
for header, width in combined:
    print(f"  {header:<6}{width:>3}")

print("-" * 40)
#header + actual rows
print(f"{len(ROWS)+1} lines   {len(combined)} columns   {character_count} characters")




