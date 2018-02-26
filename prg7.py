def main():
    nums = list(map(int, input('Enter list of numbers:').split()))
    get_non_repating_num(nums)


'''
Find non repeating num given a list, only one non repeating num is present

Args:
    l(list): l

prints: non repeating num

'''


def get_non_repating_num(l):
    non_repeating, repeating = set(), set()

    for i in l:
        if i not in non_repeating:
            non_repeating.add(i)
        else:
            repeating.add(i)

    unique_num = non_repeating.difference(repeating)
    print(unique_num)


main()
