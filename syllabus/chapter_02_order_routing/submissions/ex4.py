#Exercise 4 - Fraud risk scoring

a_id, a_raw_value, a_age, a_bill, a_ship_to, a_phone = "ORD-4001", "1240.00", 3,  "GB", "DE", None
b_id, b_raw_value, b_age, b_bill, b_ship_to, b_phone = "ORD-4002", "80.00",  400, "GB", "GB", "07700900123"
c_id, c_raw_value, c_age, c_bill, c_ship_to, c_phone = "ORD-4003", "1500.00", 90, "FR", "FR", None

a_value = float(a_raw_value)
b_value = float(b_raw_value)
c_value = float(c_raw_value)

a_points = 0
b_points = 0
c_points = 0

if a_age < 7:
    a_points += 30
if a_value > 1000:
    a_points += 25
if a_bill != a_ship_to:
    a_points += 20
if a_phone is None:
    a_points += 15

if b_age < 7:
    b_points += 30
if b_value > 1000:
    b_points += 25
if b_bill != b_ship_to:
    b_points += 20
if b_phone is None:
    b_points += 15

if c_age < 7:
    c_points += 30
if c_value > 1000:
    c_points += 25
if c_bill != c_ship_to:
    c_points += 20
if c_phone is None:
    c_points += 15


if a_points >= 50: #50 or above holds the order
    a_route = "HOLD"
elif a_points >= 25: #25 to 49 flags for review
    a_route = "REVIEW"
else: #below 25 ships
    a_route = "SHIP"

if b_points >= 50:
    b_route = "HOLD"
elif b_points >= 25:
    b_route = "REVIEW"
else:
    b_route = "SHIP"

if c_points >= 50:
    c_route = "HOLD"
elif c_points >= 25:
    c_route = "REVIEW"
else:
    c_route = "SHIP"

print(f"{a_id}{a_points:>5}  {a_route:<8}{a_value:>11,.2f}")
print(f"{b_id}{b_points:>5}  {b_route:<8}{b_value:>11,.2f}")
print(f"{c_id}{c_points:>5}  {c_route:<8}{c_value:>11,.2f}")
