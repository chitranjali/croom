def main():
    l1 = list(map(int, input('Enter list of numbers l1:').split()))
    l2 = list(map(int, input('Enter list of numbers l2:').split()))
    get_common(l1, l2)


'''
print all common numbers between two lists

Args:
    l1(list): l1, unique elements
    l2(list): l2, unique

'''


def get_common(l1, l2):
    # print([x for x in l1 if x in l2])
    common_nums, l3 = [], []
    l1.extend(l2)
    for i in l1:
        if i in l3:
            common_nums.append(i)
        else:
            l3.append(i)

    print(common_nums)


main()
