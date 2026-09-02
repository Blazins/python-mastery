#Exercise 1 - The returns desk at close of day

returns = (
    ("SKU-104", "SEALED",  99.00),
    ("SKU-101", "SEALED",  24.99),
    ("SKU-112", "DAMAGED", 45.00),
    ("SKU-107", "OPENED",   8.75),
    ("SKU-109", "SEALED",  24.99),
    ("SKU-102", "DAMAGED", 15.50),
    ("SKU-118", "OPENED",  30.00),
)

restock = []
resold = []
writeoff = []

for sku, condition, value in returns:
    if condition == "SEALED":
        restock.append(sku)
    elif condition == "OPENED":
        resold.append((sku,value/2))
    else:
        writeoff.append((sku,value))


print(f"RESTOCK ({len(restock)})")
if restock:
    for item in sorted(restock):
        print(f"  {item}")
else:
    print("  none")

print(f"INSPECT ({len(resold)})")
if resold:
    for sku, amount in sorted(resold):
        print(f"  {sku:<10}{amount:>7.2f}")
else:
    print("  none")

print(f"WRITE-OFF ({len(writeoff)})")
total = 0.00
if writeoff:
    for sku, amount in sorted(writeoff):
        print(f"  {sku:<10}{amount:>7.2f}")
        total += amount
else:
    print("  none")

print("-" * 46)
print(f"{len(returns)} returned   {len(restock)} restocked   {len(resold)} to inspect   {total:,.2f} lost")
