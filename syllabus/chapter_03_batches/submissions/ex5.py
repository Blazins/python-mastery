#Exercise 5 - The validation gauntlet, with a tally

ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-5101", "buyer@shop.co", "3", "IE"),
    ("ORD-5102", "buyer.shop.co", "2", "GB"),
    ("ORD-5103", "buyer@shop.co", "0", "GB"),
    ("ORD-5104", "buyer@shop.co", "4", "DE"),
    ("ORD-5105", "buyer@shop.co", "1", "FR"),
    ("ORD-5106", "shop.co", "0", "US"),
)
email_rejected_count = 0
dest_rejected_count = 0
qty_rejected_count = 0
accepted_count = 0

for order_id, email, raw_qty, dest in orders:
    qty =  int(raw_qty)
    if "@" not in email:
        print(f"{order_id}: REJECTED - email address is not valid")
        email_rejected_count += 1
    elif qty <= 0:
        print(f"{order_id}: REJECTED - quantity must be at least 1")
        qty_rejected_count += 1
    elif dest not in ALLOWED:
        print(f"{order_id}: REJECTED - we do not ship to {dest}")
        dest_rejected_count += 1
    else:
        print(f"{order_id}: ACCEPTED - {qty} units to {dest}")
        accepted_count += 1

print("-" * 44)
print(f"{accepted_count} accepted, {email_rejected_count + dest_rejected_count + qty_rejected_count} rejected")
print(f"  email {email_rejected_count}   quantity {qty_rejected_count}   destination {dest_rejected_count}")
