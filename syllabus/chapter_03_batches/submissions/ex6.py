#Exercise 6 - The pipeline, whole

ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-6101", "buyer@shop.co", "2", "GB", "1240.00", 3, "GB", None),
    ("ORD-6102", "buyer.shop.co", "2", "GB", "200.00", 400, "GB", "07700900123"),
    ("ORD-6103", "buyer@shop.co", "1", "IE", "640.00", 90, "IE", "07700900555"),
    ("ORD-6104", "buyer@shop.co", "5", "DE", "80.00", 12, "GB", None),
    ("ORD-6105", "buyer@shop.co", "0", "GB", "310.00", 40, "GB", "07700900777"),
    ("ORD-6106", "buyer@shop.co", "3", "FR", "300.00", 90, "GB", None),
)


rejected_count = 0
shipped_count = 0
held_count = 0
review_count = 0
dispatched_value = 0.00
dispatched_total = 0.00

for order_id, email, raw_qty, dest, raw_value, age, bill, phone_number in orders:
    qty =  int(raw_qty)
    value = float(raw_value)

    if "@" not in email:
        print(f"{order_id}  REJECTED    email address is not valid")
        rejected_count += 1
    elif qty <= 0:
        print(f"{order_id}  REJECTED    quantity must be at least 1")
        rejected_count += 1
    elif dest not in ALLOWED:
        print(f"{order_id}  REJECTED    we do not ship to {dest}")
        rejected_count += 1

    else:
        risk_points = 0

        if age < 7:
            risk_points += 30
        if value > 1000:
            risk_points += 25
        if bill != dest:
            risk_points += 20
        if phone_number is None:
            risk_points += 15



        if risk_points >= 50:
            route = "HOLD"
            held_count += 1
        elif risk_points >= 25:
            route = "REVIEW"
            review_count += 1
        else:
            route = "SHIP"
            shipped_count += 1
            dispatched_value = value

        ship = 0.00 if value >= 500 else 7.95
        total = ship + value

        print(f"{order_id}  {route:<12}risk {risk_points:>3}   {total:>9,.2f}")

print("-" * 46)
print(f"{len(orders)} orders   {shipped_count} shipped   {review_count} review   {held_count} held   {rejected_count} rejected")
print(f"dispatched value {dispatched_value:,.2f}")
