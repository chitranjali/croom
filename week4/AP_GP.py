l = [0]
while l:
    l = list(map(int, input().split()))

    if len(l) > 2:

        if (l[0] - l[1] == l[1] - l[2]):
            k = l[1] - l[0]
            print('AP', l[-1] + k)
        elif (l[1] / l[0] == l[2] / l[1]):
            k = int(l[1] / l[0])
            print('GP', l[-1] * k)
        else:
            print('None')

print('Done')