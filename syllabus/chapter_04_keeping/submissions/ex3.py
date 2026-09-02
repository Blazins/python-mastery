#Exercise 3 - The slowest endpoints

requests = (
    ("/checkout",  412),
    ("/search",   1180),
    ("/cart",       88),
    ("/product",   940),
    ("/search",   1620),
    ("/home",       35),
    ("/checkout",  770),
)

if requests:
    SLOW = 500

    slow_requests = []
    total_duration = 0.0
    fast_requests = []

    for endpoint, duration in requests:
        if duration >= SLOW:
            slow_requests.append((endpoint, duration))
        total_duration += duration
        fast_requests.append(duration)

    sorted_fast_requests = sorted(fast_requests)
    slow_requests.sort(reverse=True)
    print(f"REQUESTS OVER {SLOW}ms")

    for n, pair in enumerate(slow_requests, start = 1):
        if n > 3:
            break
        endpoint, duration = pair
        print(f"{n}. {endpoint:<12}{duration:>6}ms")

    if not slow_requests:
        print("  none")

    print("-" * 30)
    print(f"{len(requests)} requests   {len(slow_requests)} slow   fastest {sorted_fast_requests[0]}ms   mean {total_duration/len(requests):.1f}ms")

else:
    print("No requests available")



