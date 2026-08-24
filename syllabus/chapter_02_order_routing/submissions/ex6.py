#Exercise 6 - The full order pipeline

a_id, a_email, a_raw_qty, a_dest, a_raw_value, a_age, a_bill, a_phone = "ORD-6001", "buyer@shop.co", "2", "GB", "1240.00", 3,  "GB", None
b_id, b_email, b_raw_qty, b_dest, b_raw_value, b_age, b_bill, b_phone = "ORD-6002", "buyer.shop.co", "2", "GB", "200.00", 400, "GB", "07700900123"
c_id, c_email, c_raw_qty, c_dest, c_raw_value, c_age, c_bill, c_phone = "ORD-6003", "buyer@shop.co", "1", "IE", "640.00",  90, "IE", "07700900555"

a_value = float(a_raw_value)
b_value = float(b_raw_value)
c_value = float(c_raw_value)

a_qty = int(a_raw_qty)
b_qty = int(b_raw_qty)
c_qty = int(c_raw_qty)

a_ships_to = a_dest == "GB" or a_dest == "IE" or a_dest == "FR"
b_ships_to = b_dest == "GB" or b_dest == "IE" or b_dest == "FR"
c_ships_to = c_dest == "GB" or c_dest == "IE" or c_dest == "FR"

if "@" not in a_email:
    print(f"{a_id}  {'REJECTED':<12}email address is not valid")
elif a_qty <= 0:
    print(f"{a_id}  {'REJECTED':<12}quantity must be at least 1")
elif not a_ships_to:
    print(f"{a_id}  {'REJECTED':<12}we do not ship to {a_dest}")
else:
    a_points = 0

    if a_age < 7:
        a_points += 30
    if a_value > 1000:
        a_points += 25
    if a_bill != a_dest:
        a_points += 20
    if a_phone is None:
        a_points += 15

    if a_points >= 50:
        a_route = "HOLD" #holds the order
    elif a_points >= 25:
        a_route = "REVIEW" #flags for review
    else:
        a_route = "SHIP"

    a_ship_cost = 0 if a_value >= 500 else 7.95
    a_total = a_value + a_ship_cost

    print(f"{a_id}  {a_route:<12}risk {a_points:>3}   {a_total:>9,.2f}")

if "@" not in b_email:
    print(f"{b_id}  {'REJECTED':<12}email address is not valid")
elif b_qty <= 0:
    print(f"{b_id}  {'REJECTED':<12}quantity must be at least 1")
elif not b_ships_to:
    print(f"{b_id}  {'REJECTED':<12}we do not ship to {b_dest}")
else:
    b_points = 0

    if b_age < 7:
        b_points += 30
    if b_value > 1000:
        b_points += 25
    if b_bill != b_dest:
        b_points += 20
    if b_phone is None:
        b_points += 15

    if b_points >= 50:
        b_route = "HOLD" #holds the order
    elif b_points >= 25:
        b_route = "REVIEW" #flags for review
    else:
        b_route = "SHIP"

    b_ship_cost = 0 if b_value >= 500 else 7.95
    b_total = b_value + b_ship_cost

    print(f"{b_id}  {b_route:<12}risk {b_points:>3}   {b_total:>9,.2f}")

if "@" not in c_email:
    print(f"{c_id}  {'REJECTED':<12}email address is not valid")
elif c_qty <= 0:
    print(f"{c_id}  {'REJECTED':<12}quantity must be at least 1")
elif not c_ships_to:
    print(f"{c_id}  {'REJECTED':<12}we do not ship to {c_dest}")
else:
    c_points = 0

    if c_age < 7:
        c_points += 30
    if c_value > 1000:
        c_points += 25
    if c_bill != c_dest:
        c_points += 20
    if c_phone is None:
        c_points += 15

    if c_points >= 50:
        c_route = "HOLD" #holds the order
    elif c_points >= 25:
        c_route = "REVIEW" #flags for review
    else:
        c_route = "SHIP"

    c_ship_cost = 0 if c_value >= 500 else 7.95
    c_total = c_value + c_ship_cost

    print(f"{c_id}  {c_route:<12}risk {c_points:>3}   {c_total:>9,.2f}")
