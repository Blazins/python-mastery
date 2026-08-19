#The daily catalogue report

name_1, raw_cost_1, price_1, raw_qty_1 = "Blue Mug",           "4.99",  9.58,  "3"
name_2, raw_cost_2, price_2, raw_qty_2 = "Oak Chopping Board", "18.50", 41.25, "12"
name_3, raw_cost_3, price_3, raw_qty_3 = "Linen Tea Towel",    "3.20",  7.99,  "140"

product_1_cost, product_1_qty = float(raw_cost_1), int(raw_qty_1)
product_2_cost, product_2_qty = float(raw_cost_2), int(raw_qty_2)
product_3_cost, product_3_qty = float(raw_cost_3), int(raw_qty_3)

product_1_total =  price_1 * product_1_qty
product_2_total =  price_2 * product_2_qty
product_3_total =  price_3 * product_3_qty

product_1_margin = (price_1 - product_1_cost)/price_1
product_2_margin = (price_2 - product_2_cost)/price_2
product_3_margin = (price_3 - product_3_cost)/price_3

column_1 = "PRODUCT"
column_2 = "QTY"
column_3 = "COST"
column_4 = "PRICE"
column_5 = "TOTAL"
column_6 = "MARGIN"

total_word = "TOTAL"
total = product_1_total + product_2_total + product_3_total

print(f"{column_1:<20}{column_2:>5}{column_3:>10}{column_4:>10}{column_5:>12}{column_6:>9}")
print(f"------------------------------------------------------------------")
print(f"{name_1:<20}{product_1_qty:>5}{product_1_cost:>10.2f}{price_1:>10.2f}{product_1_total:>12,.2f}{product_1_margin:>9.1%}")
print(f"{name_2:<20}{product_2_qty:>5}{product_2_cost:>10.2f}{price_2:>10.2f}{product_2_total:>12,.2f}{product_2_margin:>9.1%}")
print(f"{name_3:<20}{product_3_qty:>5}{product_3_cost:>10.2f}{price_3:>10.2f}{product_3_total:>12,.2f}{product_3_margin:>9.1%}")
print(f"{total_word:<45}{total:>12,.2f}")
