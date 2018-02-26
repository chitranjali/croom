def main():
    nums = list(map(int, input('Enter list of numbers:').split()))
    x, y = map(int, input().split())
    get_sum(nums, x, y)


'''
print sum of list l excluding sublist between x and y

Args:
    l(list): l

prints: total

'''


def get_sum(l, x, y):
    # try:
    #     i = l.index(x)
    # # except:
    #     # i = -1
    # try:
    #     j = l.index(y)
    # # except:
    #     # j = -1
    #
    # low  = i if i < j else j
    # high = j if j > i else i
    # print(sum(l[0:low]) + sum(l[high+1:]))
    flag = True
    total = 0
    for i in l:
        if (i == x or i == y) and flag:
            flag = False
        elif (i == x or i == y) and not flag:
            flag = 'next'

        if flag:
            total = total + i
        if flag == 'next':
            flag = True

    print(total)


main()
