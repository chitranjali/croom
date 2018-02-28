

def main():
    s = input('Enter string:')
    get_freq(s)


'''
Given a string, print three most common characters, lexicographically

Args: 
    s(string) : s
'''


def get_freq(s):
    d = {}

    for i in s:
        d[i] = d.get(i, 0) + 1
    # sort by alphabet
    alpha_sort = sorted(d.items(), key=lambda x: (ord(x[0])))
    # Again reverse sort by occurances , stable sorting
    l1 = sorted(alpha_sort, key=lambda x: (x[1]), reverse=True)

    most_used = [i[0] for i in l1[:3]]
    print(''.join(most_used))


main()
