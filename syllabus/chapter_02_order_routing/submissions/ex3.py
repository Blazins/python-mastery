#Exercise 3 - Discount codes that may not be there

a_id, a_code, a_pct, a_raw_value = "ORD-3001", "SAVE10", "10",  "250.00"
b_id, b_code, b_pct, b_raw_value = "ORD-3002", None,     "",    "250.00"
c_id, c_code, c_pct, c_raw_value = "ORD-3003", "SAVE00", "0",   "250.00"
d_id, d_code, d_pct, d_raw_value = "ORD-3004", "SAVE20", "20",  "80.00"

a_has_discount = a_pct != "" and float(a_pct) > 0
b_has_discount = b_pct!= "" and float(b_pct) > 0
c_has_discount = c_pct != "" and float(c_pct) > 0
d_has_discount = d_pct!= "" and float(d_pct) > 0

a_order_value =  float(a_raw_value)
b_order_value =  float(b_raw_value)
c_order_value =  float(c_raw_value)
d_order_value =  float(d_raw_value)

if a_has_discount:
    a_prct = float(a_pct)
    a_discount_amt = (a_prct/100 * a_order_value) if a_order_value >= 100 else 0
    a_amt_payable = a_order_value - a_discount_amt
    a_reason_text = "applied" if a_discount_amt > 0 else "order below 100.00 minimum"
    a_rate = a_prct if a_order_value >= 100 else 0.0
elif a_code is None:
    a_reason_text = "no code supplied"
    a_rate = 0.0
    a_discount_amt = 0
    a_amt_payable = a_order_value
elif a_pct == "":
    a_reason_text = "code has no percentage"
    a_rate = 0.0
    a_discount_amt = 0
    a_amt_payable = a_order_value
elif a_prct <= 0:
    a_reason_text = "percentage is zero"
    a_rate = 0.0
    a_discount_amt = 0
    a_amt_payable = a_order_value
elif a_order_value < 100:
    a_reason_text = "order below 100.00 minimum"
    a_rate = 0.0
    a_discount_amt = 0
    a_amt_payable = a_order_value

if b_has_discount:
    b_prct = float(b_pct)
    b_discount_amt = (b_prct/100 * b_order_value) if b_order_value >= 100 else 0
    b_amt_payable = b_order_value - b_discount_amt
    b_reason_text = "applied" if b_discount_amt > 0 else "order below 100.00 minimum"
    b_rate = b_prct if b_order_value >= 100 else 0.0
elif b_code is None:
    b_reason_text = "no code supplied"
    b_rate = 0.0
    b_discount_amt = 0
    b_amt_payable = b_order_value
elif b_pct == "":
    b_reason_text = "code has no percentage"
    b_rate = 0.0
    b_discount_amt = 0
    b_amt_payable = c_order_value
elif b_prct <= 0:
    b_reason_text = "percentage is zero"
    b_rate = 0.0
    b_discount_amt = 0
    b_amt_payable = b_order_value
elif b_order_value < 100:
    b_reason_text = "order below 100.00 minimum"
    b_rate = 0.0
    b_discount_amt = 0
    b_amt_payable = b_order_value

if c_has_discount:
    c_prct = float(c_pct)
    c_discount_amt = (c_prct/100 * c_order_value) if c_order_value >= 100 else 0
    c_amt_payable = c_order_value - c_discount_amt
    c_reason_text = "applied" if c_discount_amt > 0 else "order below 100.00 minimum"
    c_rate = c_prct if c_order_value >= 100 else 0.0
elif c_code is None:
    c_reason_text = "no code supplied"
    c_rate = 0.0
    c_discount_amt = 0
    c_amt_payable = c_order_value
elif c_pct == "":
    c_reason_text = "code has no percentage"
    c_rate = 0.0
    c_discount_amt = 0
    c_amt_payable = c_order_value
elif c_pct is "0":
    c_reason_text = "percentage is zero"
    c_rate = 0.0
    c_discount_amt = 0
    c_amt_payable = c_order_value
elif c_order_value < 100:
    c_reason_text = "order below 100.00 minimum"
    c_rate = 0.0
    c_discount_amt = 0
    c_amt_payable = c_order_value

if d_has_discount:
    d_prct = float(d_pct)
    d_discount_amt = (d_prct/100 * d_order_value) if d_order_value >= 100 else 0
    d_amt_payable = d_order_value - d_discount_amt
    d_reason_text = "applied" if d_discount_amt > 0 else "order below 100.00 minimum"
    d_rate = d_prct if d_order_value >= 100 else 0.0
elif d_code is None:
    d_reason_text = "no code supplied"
    d_rate = 0.0
    d_discount_amt = 0
    d_amt_payable = d_order_value
elif d_pct == "":
    d_reason_text = "code has no percentage"
    d_rate = 0.0
    d_discount_amt = 0
    d_amt_payable = d_order_value
elif d_prct <= 0:
    d_reason_text = "percentage is zero"
    d_rate = 0.0
    d_discount_amt = 0
    d_amt_payable = d_order_value
elif d_order_value < 100:
    d_reason_text = "order below 100.00 minimum"
    d_rate = 0.0
    d_discount_amt = 0
    d_amt_payable = d_order_value


print(f"{a_id}  {a_reason_text:<26}{a_prct:>6.1f}%{a_discount_amt:>9,.2f}{a_amt_payable:>10,.2f}")
print(f"{b_id}  {b_reason_text:<26}{b_rate:>6.1f}%{b_discount_amt:>9,.2f}{b_amt_payable:>10,.2f}")
print(f"{c_id}  {c_reason_text:<26}{c_rate:>6.1f}%{c_discount_amt:>9,.2f}{c_amt_payable:>10,.2f}")
print(f"{d_id}  {d_reason_text:<26}{d_rate:>6.1f}%{d_discount_amt:>9,.2f}{d_amt_payable:>10,.2f}")

