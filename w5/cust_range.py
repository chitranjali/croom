def custom_range(n):
    i = 0
    while i < n:
        yield i
        i = i + 1

for i in custom_range(5):
    print(i)
