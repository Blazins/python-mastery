#Exercise 5 - Deduplicating a supplier feed

feed = (
    "SKU-301", "SKU-302", "SKU-301", "SKU-303",
    "SKU-302", "SKU-301", "SKU-304",
)

unique_skus = []
repeated_skus = []
first_position = []

for i,sku in enumerate(feed):
    if sku not in unique_skus:
        unique_skus.append(sku)
    else:
        repeated_skus.append((i,sku))

print(f"UNIQUE ({len(unique_skus)})")
for n, sku in enumerate(unique_skus, start = 1):
    print(f"{n}. {sku}")

print("REPEATS")

for sku in unique_skus:
    for i in range(len(feed)):
        if feed[i] == sku:
            first_position.append((i, sku))


if repeated_skus:
    for position, sku in repeated_skus:
        for i, sku_id in first_position:
            if sku_id == sku:
                print(f"  {sku} first seen at {i}, again at {position}")
                break

else:
    print("  no duplicates")

print("-" * 34)
print(f"{len(feed)} rows   {len(unique_skus)} unique   {len(repeated_skus)} repeats")

