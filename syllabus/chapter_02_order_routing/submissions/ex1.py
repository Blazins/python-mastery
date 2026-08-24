#Exercise 1 - Shipping bands across a batch

a_id, a_raw = "ORD-1001", "642.50"
b_id, b_raw = "ORD-1002", "120.00"
c_id, c_raw = "ORD-1003", "500.00"

a_value = float(a_raw)
b_value = float(b_raw)
c_value = float(c_raw)

#one block per order
if a_value >= 500:
    a_shipping_cost = 0.00
    a_band = "FREE"
elif a_value >= 100:
    a_shipping_cost = 3.95
    a_band = "STANDARD"
elif a_value >= 25:
    a_shipping_cost = 5.95
    a_band = "SMALL"
else:
    a_shipping_cost = 7.95
    a_band = "MINIMUM"

#one block per order
if b_value >= 500:
    b_shipping_cost = 0.00
    b_band = "FREE"
elif b_value >= 100:
    b_shipping_cost = 3.95
    b_band = "STANDARD"
elif b_value >= 25:
    b_shipping_cost = 5.95
    b_band = "SMALL"
else:
    b_shipping_cost = 7.95
    b_band = "MINIMUM"

#one block per order
if c_value >= 500:
    c_shipping_cost = 0.00
    c_band = "FREE"
elif c_value >= 100:
    c_shipping_cost = 3.95
    c_band = "STANDARD"
elif c_value >= 25:
    c_shipping_cost = 5.95
    c_band = "SMALL"
else:
    c_shipping_cost = 7.95
    c_band = "MINIMUM"

print(f"{'ORDER':<10}{'VALUE':>10}  {'BAND':<10}{'SHIP':>6}{'TOTAL':>11}")
print("-" * 47)
print(f"{a_id:<10}{a_value:>10,.2f}  {a_band:<10}{a_shipping_cost:>6.2f}{a_value + a_shipping_cost:>11,.2f}")
print(f"{b_id:<10}{b_value:>10,.2f}  {b_band:<10}{b_shipping_cost:>6.2f}{b_value + b_shipping_cost:>11,.2f}")
print(f"{c_id:<10}{c_value:>10,.2f}  {c_band:<10}{c_shipping_cost:>6.2f}{c_value + c_shipping_cost:>11,.2f}")
