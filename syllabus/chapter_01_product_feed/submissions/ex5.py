#Margin against markup

raw_cost  = "18.50"   # as text from the feed
raw_price = "41.25"   # as text from the feed

cost = float(raw_cost)
price = float(raw_price)
profit = price - cost
margin = profit / price
markup = profit / cost

gap = (markup - margin) * 100
print(f"Cost:            £{cost:.2f}")
print(f"Price:           £{price:.2f}")
print(f"Margin:          {margin:.1%}")
print(f"Markup:          {markup:.1%}")
print(f"Gap:             {gap:.1f} percentage points")
