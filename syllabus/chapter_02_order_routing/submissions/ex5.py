#Exercise 5 - Warehouse handling and dispatch priority

a_sku, a_raw_w, a_fragile, a_dest, a_raw_value = "SKU-5001", "2.5",  True,  "GB", "480.00"
b_sku, b_raw_w, b_fragile, b_dest, b_raw_value = "SKU-5002", None,   False, "FR", "1200.00"
c_sku, c_raw_w, c_fragile, c_dest, c_raw_value = "SKU-5003", "31.0", False, "GB", "95.00"

a_value = float(a_raw_value)
b_value = float(b_raw_value)
c_value = float(c_raw_value)


if a_raw_w is None:
    a_handling = "WEIGH"
else:
    a_w = float(a_raw_w)
    if a_w >= 30:
        a_handling = "TWO-PERSON"
    elif a_fragile:
        a_handling = "FRAGILE"
    else:
        a_handling = "STANDARD"


if b_raw_w is None:
    b_handling = "WEIGH"
else:
    b_w = float(b_raw_w)
    if b_w >= 30:
        b_handling = "TWO-PERSON"
    elif b_fragile:
        b_handling = "FRAGILE"
    else:
        b_handling = "STANDARD"
    
if c_raw_w is None:
    c_handling = "WEIGH"
else:
    c_w = float(c_raw_w)
    if c_w >= 30:
        c_handling = "TWO-PERSON"
    elif c_fragile:
        c_handling = "FRAGILE"
    else:
        c_handling = "STANDARD"


if a_value >= 1000:
    a_priority = "EXPRESS"
elif a_value >= 100:
    a_priority = "PRIORITY"
else:
    a_priority = "ECONOMY"

if b_value >= 1000:
    b_priority = "EXPRESS"
elif b_value >= 100:
    b_priority = "PRIORITY"
else:
    b_priority = "ECONOMY"

if c_value >= 1000:
    c_priority = "EXPRESS"
elif c_value >= 100:
    c_priority = "PRIORITY"
else:
    c_priority = "ECONOMY"

is_a_domestic = "Y" if a_dest == "GB" else "N"
is_b_domestic = "Y" if b_dest == "GB" else "N"
is_c_domestic = "Y" if c_dest == "GB" else "N"

if a_raw_w is not None:
    print(f"{a_sku}{a_w:>6.1f}  {a_handling:<12}{a_priority:<10}{is_a_domestic}")
else:
    print(f"{a_sku}{'--':^6}  {a_handling:<12}{a_priority:<10}{is_a_domestic}")
if b_raw_w is not None:
    print(f"{b_sku}{b_w:>6.1f}  {b_handling:<12}{b_priority:<10}{is_b_domestic}")
else:
    print(f"{b_sku}{'--':^6}  {b_handling:<12}{b_priority:<10}{is_b_domestic}")
if c_raw_w is not None:
    print(f"{c_sku}{c_w:>6.1f}  {c_handling:<12}{c_priority:<10}{is_c_domestic}")
else:
    print(f"{c_sku}{'--':^6}  {c_handling:<12}{c_priority:<10}{is_c_domestic}")



