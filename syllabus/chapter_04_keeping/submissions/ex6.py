ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-8101", "a@shop.co", "GB", "1240.00",   3, "GB", None),
    ("ORD-8102", "bad.email", "GB",  "200.00", 400, "GB", "07700900123"),
    ("ORD-8103", "c@shop.co", "IE",  "640.00",  90, "IE", "07700900555"),
    ("ORD-8104", "d@shop.co", "DE",   "80.00",  12, "GB", None),
    ("ORD-8105", "e@shop.co", "FR",  "300.00",  90, "GB", None),
    ("ORD-8106", "f@shop.co", "GB",  "920.00",   2, "FR", None),
    ("ORD-8107", "g@shop.co", "IE",   "45.00", 200, "IE", "07700900999"),
)

email_rejected = []
dest_rejected = []
rejected_count = 0
held_count = 0
review_count = 0
ship_count = 0
held = []
review = []
ship = []
total = 0.00
total_dispatched = 0.00

for order_id, email, dest, value, account_age_days, billing_country, phone in orders:
    if "@" not in email:
        reason = "email address is not valid"
        email_rejected.append((order_id, reason))
        rejected_count += 1
    elif dest not in ALLOWED:
        reason = "we do not ship to"
        dest_rejected.append((order_id, dest, reason))
        rejected_count += 1

    else:
        float_value = float(value)
        risk_score = 0
        if account_age_days <= 7:
            risk_score += 30
        if float_value >= 1000.00:
            risk_score += 25
        if billing_country != dest:
            risk_score += 20
        if phone is None:
            risk_score += 15

        if risk_score >= 50:
            held.append((risk_score, order_id))
            held_count += 1
        elif risk_score >= 25:
            review.append((risk_score, order_id))
            review_count += 1
        else:
            if float_value >= 500.00:
                ship_cost = 0.00
            else:
                ship_cost = 7.95
            total = float_value + ship_cost
            ship.append((total, order_id))
            ship_count += 1

print("HELD")
if held:
    for risk_points, order_id in sorted(held, reverse = True):
        print(f"  {order_id}  risk {risk_points:>3}")
else:
    print("  none")

print("REVIEW")
if review:
    for risk_points, order_id in sorted(review, reverse = True):
        print(f"  {order_id}  risk {risk_points:>3}")
else:
    print("  none")

print("REJECTED")
if email_rejected or dest_rejected:
    for order_id, reason in sorted(email_rejected):
        print(f"  {order_id}  {reason}")

    for order_id, dest, reason in sorted(dest_rejected):
        print(f"  {order_id}  {reason} {dest}")
else:
    print("  none")

print("SHIPPED")
if ship:
    for total, order_id in sorted(ship, reverse = True):
        print(f"  {order_id}  {total:>9,.2f}")
        total_dispatched += total
else:
    print("  none")

print("-" * 46)
print(f"{len(orders)} orders   {ship_count} shipped   {review_count} review   {held_count} held   {rejected_count} rejected")
print(f"dispatched {total_dispatched:,.2f}")

