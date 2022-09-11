def parse_times(FULLY_SYNCED_NOTIFICATIONS_EVERY_X_HOURS):
    times = []
    for x in range(24):
        try:
            if x % FULLY_SYNCED_NOTIFICATIONS_EVERY_X_HOURS == 0:
                times.append(x)
        except ZeroDivisionError:
            pass

    times_sorted = sorted([x - 24 if x > 24 else x for x in times])

    for x in times_sorted:
        if (
            (FULLY_SYNCED_NOTIFICATIONS_EVERY_X_HOURS > 12) or (x * 2 > 12)
        ) and 0 in times_sorted:
            times_sorted.remove(0)

    times_sent = {str(x): False for x in times_sorted}
    return times, times_sent
