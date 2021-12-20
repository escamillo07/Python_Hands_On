per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes = total_seconds // 60
seconds = total_seconds % 60
print("{} minutes and {} seconds".format(minutes,seconds))