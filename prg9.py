def main():
    s = input('Enter string:')
    n = int(input('Enter N:'))

    sub_strings = []
    slice_str(s, n, sub_strings)


'''
Given a string and a num,which divides s in multiple substrings,
print output without duplicate chars

Args: 
    s(string) : s
    n(int): n
    l(list) : list of substrings
'''


def slice_str(s, n, l):
    if len(s) > n:
        l.append(''.join(dict.fromkeys((s[0:n]), 0)))
        return slice_str(s[n:], n, l)
    else:
        l.append(''.join(dict.fromkeys(s, 0)))

    print('\n'.join(l))


main()
