#Exercise 2 - The validation gauntlet

a_id, a_email, a_raw_qty, a_dest = "ORD-2001", "mike@example.com", "3",  "IE"
b_id, b_email, b_raw_qty, b_dest = "ORD-2002", "mike.example.com", "3",  "GB"
c_id, c_email, c_raw_qty, c_dest = "ORD-2003", "buyer@shop.co",   "0",  "GB"
d_id, d_email, d_raw_qty, d_dest = "ORD-2004", "buyer@shop.co",   "2",  "DE"


a_qty = int(a_raw_qty)
b_qty = int(b_raw_qty)
c_qty = int(c_raw_qty)
d_qty = int(d_raw_qty)

a_destination_allowed = a_dest == "GB" or a_dest == "IE" or a_dest == "FR"
b_destination_allowed = b_dest == "GB" or b_dest == "IE" or b_dest == "FR"
c_destination_allowed = c_dest == "GB" or c_dest == "IE" or c_dest == "FR"
d_destination_allowed = d_dest == "GB" or d_dest == "IE" or d_dest == "FR"


if "@" not in a_email:
    print(f"{a_id}: REJECTED - email address is not valid") 
elif a_qty <= 0:
    print(f"{a_id}: REJECTED - quantity must be at least 1")
elif not a_destination_allowed:
    print(f"{a_id}: REJECTED - we do not ship to {a_dest}")
else:
    print(f"{a_id}: ACCEPTED - {a_qty} units to {a_dest}")

if "@" not in b_email:
    print(f"{b_id}: REJECTED - email address is not valid") 
elif b_qty <= 0:
    print(f"{b_id}: REJECTED - quantity must be at least 1")
elif not b_destination_allowed:
    print(f"{b_id}: REJECTED - we do not ship to {b_dest}")
else:
    print(f"{b_id}: ACCEPTED - {b_qty} units to {b_dest}")

if "@" not in c_email:
    print(f"{c_id}: REJECTED - email address is not valid") 
elif c_qty <= 0:
    print(f"{c_id}: REJECTED - quantity must be at least 1")
elif not c_destination_allowed:
    print(f"{c_id}: REJECTED - we do not ship to {c_dest}")
else:
    print(f"{c_id}: ACCEPTED - {c_qty} units to {c_dest}")
    
if "@" not in d_email:
    print(f"{d_id}: REJECTED - email address is not valid") 
elif d_qty <= 0:
    print(f"{d_id}: REJECTED - quantity must be at least 1")
elif not d_destination_allowed:
    print(f"{d_id}: REJECTED - we do not ship to {d_dest}")
else:
    print(f"{d_id}: ACCEPTED - {d_qty} units to {d_dest}")
