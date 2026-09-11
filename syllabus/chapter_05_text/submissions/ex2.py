#Exercise 2 - Triaging a log

log = (
    "2026-09-01 09:14:02 INFO  checkout completed for ORD-8101",
    "2026-09-01 09:14:07 WARN  slow query on /search took 1620ms",
    "2026-09-01 09:15:31 ERROR payment gateway timeout for ORD-8102",
    "2026-09-01 09:16:00 INFO  cart updated",
    "2026-09-01 09:17:45 ERROR payment gateway timeout for ORD-8103",
    "2026-09-01 09:18:12 WARN  slow query on /product took 940ms",
)

LEVEL = "ERROR"
level_entries = []
info_entries = 0
warn_entries = 0
unique_levels = []
levels_counts = []

for entry in log:
    log_entry = entry.strip()
    #print(log_entry)
    timestamp = log_entry[:20].strip()
    times = timestamp[10:]
    message = log_entry[26:].strip()
    level = log_entry[20:25].strip()


    if level not in unique_levels:
        unique_levels.append(level)


    if level == LEVEL:
        level_entries.append((times, message))
    elif level == "INFO":
        info_entries += 1
    elif level == "WARN":
        warn_entries += 1

for each_level in unique_levels:
    level_count = 0
    for entry in log:
        log_level = entry[20:25].strip()
        if log_level == each_level:
            level_count += 1
    levels_counts.append((each_level, level_count))

print(f"{LEVEL} ENTRIES ({len(level_entries)})")
if level_entries:
    for time, message in level_entries:
        print(f" {time}  {message}")
else:
    print("  none")

print("BY LEVEL")


for level, count in levels_counts:
    print(f"  {level:<6}{count:>3}")


print("-" * 40)
print(f"{len(log)} lines   {len(unique_levels)} levels   {len(level_entries)} {LEVEL.lower()}")
