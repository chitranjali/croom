from math import inf


def main():
    nums = list(map(int, input('Enter list of numbers:').split()))
    get_second_highest(nums)


'''
print second highest from list

Args:
    l(list): l

'''


def get_second_highest(l):
    # l.sort() O(nlogn)
    # print(l[-2])
    highest, second_highest = (-inf), (-inf)
    for i in l:  # O(n)
        if i > highest:
            highest, second_highest = i, highest
        elif i > second_highest:
            second_highest = i

    print(second_highest)


main()
