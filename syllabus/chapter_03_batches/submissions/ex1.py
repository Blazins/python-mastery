#Exercise 1 - A shipping report with totals

orders = (
    ("ORD-1101", "642.50"),
    ("ORD-1102", "120.00"),
    ("ORD-1103", "18.99"),
    ("ORD-1104", "500.00"),
    ("ORD-1105", "64.00"),
)

print(f"{'ORDER':<10}{'GOODS':>10}  {'BAND':<12}{'SHIP':>5}{'TOTAL':>11}")
print("-" * 50)

cum_value = 0.00
cum_cost = 0.00
cum_total = 0.00

for order_id, raw_value in orders:
    value = float(raw_value)
    if value >= 500:
        band = "FREE"
        cost = 0.00
    elif value >= 100:
        band = "STANDARD"
        cost = 3.95
    elif value >= 25:
        band = "SMALL"
        cost = 5.95
    else:
        band = "MINIMUM"
        cost = 7.95

    total = value + cost

    print(f"{order_id:<10}{value:>10,.2f}  {band:<12}{cost:>5.2f}{total:>11,.2f}")
    cum_value += value
    cum_cost += cost
    cum_total += total


print("-" * 50)
print(f"{len(orders)} orders   goods {cum_value:,.2f}   shipping {cum_cost:,.2f}   total {cum_total:,.2f}")
