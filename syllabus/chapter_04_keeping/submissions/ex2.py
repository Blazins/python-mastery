#Exercise 2 - A picking route in aisle order

picks = (
    ("SKU-330", 4, 12),
    ("SKU-118", 1,  3),
    ("SKU-207", 2,  9),
    ("SKU-441", 1, 15),
    ("SKU-092", 4,  2),
    ("SKU-655", 2,  1),
)

if picks:
    print(f"{'STOP':<6}{'AISLE':>5}{'SHELF':>7}   {'SKU'}")
    print("-" * 34)

    reorder_aisle = []
    aisles = []
    distinct_aisles = []

    for sku, aisle, shelf in picks:
        reorder_aisle.append((aisle, shelf, sku))
        aisles.append(aisle)

    reorder_aisle.sort()
    distinct_aisle_count = 0

    for aisle in aisles:
        if aisle not in distinct_aisles:
            distinct_aisles.append(aisle)
            distinct_aisle_count += 1

    for n,(aisle, shelf, sku) in enumerate(reorder_aisle, start = 1):
        print(f"{n:<6}{aisle:>5}{shelf:>7}   {sku}")

    print("-" * 34)
    print(f"{len(picks)} stops across {distinct_aisle_count} aisles")

else:
    print("nothing to pick")
