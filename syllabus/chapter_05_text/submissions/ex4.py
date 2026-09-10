paths = (
    "reports/2026/september/stock.csv",
    "stock.csv",
    "reports/2026/",
    "reports//stock.csv",
    "reports/2026/september/archive/old.stock.csv",
)

parsed = []
odd_path = []

for path in paths:
    last_slash_index = -1
    for i in range(len(path)):
        if path[i] == '/':
            last_slash_index = i

    if last_slash_index == -1:
        folder = "."
        filename = path

    else:
        folder = path[:last_slash_index]
        filename = path[last_slash_index + 1:]

    if not filename:
        folder = path[:last_slash_index+1]
        filename = "no filename"
        odd_path.append((folder, filename))
        continue


    last_period_index = -1
    for j in range(len(filename)):
        if filename[j] == ".":
            last_period_index = j
    if last_period_index == -1:
        stem = filename
        extension = "no extension"
        odd_path.append((stem, extension))
    else:
        stem = filename[:last_period_index]
        extension = filename[last_period_index + 1:]

        parsed.append((folder, stem, extension))

print(f"PARSED ({len(parsed)})")
for folder, stem, ext in parsed:
    print(f"  {folder:<34}{stem:<14}{ext}")

print("ODD")
for folder, filename in odd_path:
    print(f"  {folder:<34}{filename:<14}")

print("-" * 52)
print(f"{len(paths)} paths   {len(parsed)} parsed   {len(odd_path)} odd")
