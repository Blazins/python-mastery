#Exercise 3 - Duplicate rows in a supplier feed

feed = ("SKU-301", "SKU-302", "SKU-301", "SKU-303", "SKU-302", "SKU-301")
pairs = 0

for i in range(len(feed)):
    for j in range(i+1, len(feed)):
        if feed[i] == feed[j]:
            print(f"{feed[i]} repeats at positions {i} and {j}")
            pairs += 1

print("-" * 38)
print(f"{len(feed)} rows, {pairs} duplicate pairs")
