#Exercise 3 - Discount codes that may not be there

a_id, a_code, a_pct, a_raw_value = "ORD-3001", "SAVE10", "10",  "250.00"
b_id, b_code, b_pct, b_raw_value = "ORD-3002", None,     "",    "250.00"
c_id, c_code, c_pct, c_raw_value = "ORD-3003", "SAVE00", "0",   "250.00"
d_id, d_code, d_pct, d_raw_value = "ORD-3004", "SAVE20", "20",  "80.00"

a_order_value =  float(a_raw_value)
b_order_value =  float(b_raw_value)
c_order_value =  float(c_raw_value)
d_order_value =  float(d_raw_value)


if a_code is None:
    a_rate = 0.0
    a_reason_text = "no code supplied"
    
elif a_pct == "":
    a_rate = 0.0
    a_reason_text = "code has no percentage"
   
elif float(a_pct) <= 0:
    a_rate = 0.0
    a_reason_text = "percentage is zero"

elif a_order_value < 100.00:
    a_rate = 0.0
    a_reason_text = "order below 100.00 minimum"

else:
    a_rate = float(a_pct)
    a_reason_text = "applied"

a_discount_amt = a_rate/100 * a_order_value
a_amt_payable = a_order_value - a_discount_amt

if b_code is None:
    b_rate = 0.0
    b_reason_text = "no code supplied"

elif b_pct == "":
    b_rate = 0.0
    b_reason_text = "code has no percentage"

elif float(b_pct) <= 0:
    b_rate = 0.0
    b_reason_text = "percentage is zero"

elif b_order_value < 100.00:
    b_rate = 0.0
    b_reason_text = "order below 100.00 minimum"

else:
    b_rate = float(b_pct)
    b_reason_text = "applied"
    
b_discount_amt = b_rate/100 * b_order_value
b_amt_payable = b_order_value - b_discount_amt

if c_code is None:
    c_rate = 0.0
    c_reason_text = "no code supplied"

elif c_pct == "":
    c_rate = 0.0
    c_reason_text = "code has no percentage"

elif float(c_pct) <= 0:
    c_rate = 0.0
    c_reason_text = "percentage is zero"

elif c_order_value < 100.00:
    c_rate = 0.0
    c_reason_text = "order below 100.00 minimum"

else:
    c_rate = float(c_pct)
    c_reason_text = "applied"

c_discount_amt = c_rate/100 * c_order_value
c_amt_payable = c_order_value - c_discount_amt

if d_code is None:
    d_rate = 0.0
    d_reason_text = "no code supplied"

elif d_pct == "":
    d_rate = 0.0
    d_reason_text = "code has no percentage"

elif float(d_pct) <= 0:
    d_rate = 0.0
    d_reason_text = "percentage is zero"

elif d_order_value < 100.00:
    d_rate = 0.0
    d_reason_text = "order below 100.00 minimum"

else:
    d_rate = float(d_pct)
    d_reason_text = "applied"

d_discount_amt = d_rate/100 * d_order_value
d_amt_payable = d_order_value - d_discount_amt

print(f"{a_id}  {a_reason_text:<26}{a_rate:>6.1f}%{a_discount_amt:>9,.2f}{a_amt_payable:>10,.2f}")
print(f"{b_id}  {b_reason_text:<26}{b_rate:>6.1f}%{b_discount_amt:>9,.2f}{b_amt_payable:>10,.2f}")
print(f"{c_id}  {c_reason_text:<26}{c_rate:>6.1f}%{c_discount_amt:>9,.2f}{c_amt_payable:>10,.2f}")
print(f"{d_id}  {d_reason_text:<26}{d_rate:>6.1f}%{d_discount_amt:>9,.2f}{d_amt_payable:>10,.2f}")

