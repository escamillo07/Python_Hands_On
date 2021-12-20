per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes = total_seconds // 60
seconds = total_seconds % 60
print("{} minutes and {} seconds".format(minutes,seconds))


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(5)
print('x is now', x)
