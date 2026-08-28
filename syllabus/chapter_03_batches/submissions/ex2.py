#Exercise 2 - A reorder scan that skips and stops

stock = (
    ("SKU-201", 140, 50, True),
    ("SKU-202", 12, 40, True),
    ("SKU-203", 88, 20, False),
    ("SKU-204", 0, 30, True),
    ("SKU-205", 5, 25, True),
)

stock_out = None
reorder_count = 0
skipped_count = 0
reorder_total = 0

for sku, on_hand, reorder_level, active in stock:
    if active:
        if on_hand == 0:
            print(f"{sku}  {'STOCKOUT':<12}scan halted")
            stock_out = sku
            break
        elif on_hand <= reorder_level:
            reorder_qty = (2 * reorder_level) - on_hand
            print(f"{sku}  {'REORDER':<12}{reorder_qty} units")
            reorder_count += 1
            reorder_total += reorder_qty
        else:
            print(f"{sku}  {'OK':<12}{on_hand} on hand")

        if stock_out is None:
            continue
    
    else:
        print(f"{sku}  {'SKIPPED':<12}discontinued")
        skipped_count += 1

print("-" * 38)
print(f"halted at {stock_out}: {reorder_count} reorder lines, {reorder_total} units, {skipped_count} skipped")





