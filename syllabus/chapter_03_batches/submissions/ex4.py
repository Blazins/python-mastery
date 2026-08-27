#Exercise 4 - Stock depletion forecast

sku = "SKU-401"
stock = 90
weekly_demand = 34
weekly_restock = 20
week = 0

weekly_shortfall = weekly_demand - weekly_restock

for i in range(12):
    print(f"week {i+1:>2}  stock {stock - weekly_shortfall:>4}")
    stock = stock - weekly_shortfall
    if stock <= weekly_shortfall:
        print(f"week {i+2:>2}  stock {0:>4}")
        break

print("-" * 26)
print(f"{sku} runs out in week {i + 2}")


