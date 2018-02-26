'''
Turn l2(list of tuples) in to dict(Use Zip)
'''


def main():
    d1 = {'a': 1, 'x': 5, 'y': 10, 'b': 2, 'c': 3}
    l2 = sorted(d1.items(), key=lambda item: item[1])
    print(l2)

    # use zip:
    d2 = {item[0]: item[1] for item in l2}
    # d2 = dict(zip() # --> ?
    print(d2)


main()
