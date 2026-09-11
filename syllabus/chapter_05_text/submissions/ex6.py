ALLOWED = ("GB", "IE", "FR")

feed = (
    "ORD-9101|a@shop.co|GB|1240.00|3",
    "ORD-9102|bad.email|GB|200.00|400",
    "  ord-9103 | C@Shop.co | ie | 640.00 | 90 ",
    "ORD-9104|d@shop.co|DE|80.00|12",
    "ORD-9105|e@shop.co|FR|abc|90",
    "ORD-9103|c@shop.co|IE|640.00|90",
    "ORD-9106|f@shop.co|GB|920.00",
)
new_feed = []
rejected = []
first_orders = []
accepted = []
total_banked = 0.00

for line in feed:
    new_line = line.strip().split("|")

    cleaned_lines = []
    for item in new_line:
        cleaned_lines.append(item.strip())

    if len(cleaned_lines) != 5:
        reason = f"expected 5 fields, found {len(cleaned_lines)}"
        rejected_line = "|".join(cleaned_lines)
        rejected.append((rejected_line, reason))
        #print(rejected)
        continue

    order_id, email, destination, value, account_age_days = cleaned_lines
    new_order_id = order_id.upper()
    new_destination = destination.upper()
    new_email = email.lower()

    #print(order_id, new_email)


    if new_order_id not in first_orders:
        first_orders.append(new_order_id)
    else:
        reason = "duplicate order"
        rejected.append((new_order_id, reason))
        continue

    #print(first_orders)

    if "@" not in new_email:
        reason = "email address is not valid"
        rejected.append((new_order_id, reason))
        continue
    if new_destination not in ALLOWED:
        reason = f"we do not ship to {new_destination}"
        rejected.append((new_order_id, reason))
        continue

    if not account_age_days.isdigit():
        reason = "account age is not a number"
        rejected.append((new_order_id, reason))
        continue

    value_check = value.replace(".","")

    if not value_check.isdigit():
        reason = "value is not a number"
        rejected.append((new_order_id, reason))
        continue

    else:
        actual_value = float(value)
        account_age = int(account_age_days)

        risk_score = 0
        if account_age < 7:
            risk_score += 30
        if actual_value > 1000.00:
            risk_score += 25

        accepted.append((risk_score, new_order_id, new_destination, actual_value))
        total_banked += actual_value




print(f"ACCEPTED ({len(accepted)})")
if accepted:
    accepted_sorted = sorted(accepted, reverse = True)
    for risk_score, ord_id, dest, val in accepted_sorted:
        print(f"  {ord_id:<10}{dest:<4}{val:>10,.2f}   {'risk':>3} {risk_score:>3}")
else:
    print("  none")


print(f"REJECTED ({len(rejected)})")
if rejected:
    for order, reason in rejected:
        print(f"  {order:<34}{reason}")
else:
    print("  none")


print("-" * 50)
print(f"{len(feed)} lines   {len(accepted)} accepted   {len(rejected)} rejected   banked {total_banked:,.2f}")
