#Exercise 4 - Stock depletion forecast

sku = "SKU-401"
stock = 90
weekly_demand = 34
weekly_restock = 20
week = 0

weekly_shortfall = weekly_demand - weekly_restock

for week in range(12):
    stock -= weekly_shortfall
    if stock <= 0:
        break
    else:
        print(f"week {week+1:>2}  stock {stock:>4}")
        if stock <= weekly_shortfall:
            print(f"week {week+2:>2}  stock {0:>4}")
            break

print("-" * 26)

if stock > weekly_shortfall:
    print(f"{sku} hasn't run out")
elif stock <= 0:
    print(f"{sku} run out")
else:
    print(f"{sku} runs out in week {week + 2}")


