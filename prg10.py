from string import ascii_lowercase


def main():
    n = 0
    while n not in range(1, 26):
        n = int(input('Enter N[0-26]:'))

    print_pattern(n - 1)


'''
Given a size, print pattern

Args: 
    n(int): n (0 < n < 27 )
'''


def print_pattern(n):
    lower_case = ascii_lowercase  # abcde

    size, i = n + 1, n + 1

    while n >= 0:  # First
        print('_' * n + lower_case[i:size][::-1] + lower_case[n] +
              lower_case[i:size] + '_' * n)
        i = n
        n -= 1

    n = 1
    i = n + 1
    while n < size:  # Reverse
        print('_' * n + lower_case[i:size][::-1] + lower_case[n] +
              lower_case[i:size] + '_' * n)
        n += 1
        i = n + 1


main()
