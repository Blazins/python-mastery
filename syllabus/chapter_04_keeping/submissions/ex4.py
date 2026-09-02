#Exercise 4 - Reconciling two feeds

expected = (
    ("SKU-101", 120),
    ("SKU-104",  40),
    ("SKU-109",  75),
    ("SKU-112",  12),
    ("SKU-118",  60),
)

counted = (
    ("SKU-101", 118),
    ("SKU-104",  40),
    ("SKU-109",  80),
    ("SKU-112",  12),
    ("SKU-118",  55),
)
if len(expected) != len(counted):
    print(f"FEED MISMATCH: {len(expected)} expected rows, {len(counted)} counted rows")

short_count = 0
over_count = 0
net = 0
discrepancies = []

print("DISCREPANCIES")
for expect, count in zip(expected,counted):
    expect_sku, expect_quantity = expect
    count_sku, count_quantity = count

    if expect_sku == count_sku:
        if expect_quantity != count_quantity:
            difference = count_quantity - expect_quantity
            discrepancies.append((expect_sku, difference))
            net += difference
    else:
        print("Non matching rows")

for sku, difference in discrepancies:
    if difference > 0:
        over_count += 1
        print(f"  {sku:<10}{difference:>+5}")
    else:
        short_count += 1
        print(f"  {sku:<10}{difference:>+5}")

if not discrepancies:
    print("  none")



print("-" * 30)
print(f"{short_count} short   {over_count} over   net {net:+}")





