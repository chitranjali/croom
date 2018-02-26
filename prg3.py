from math import ceil, sqrt


def main():
    n = int(input('Enter n:'))
    get_primes(n)


'''
prints all primes till n!

Args:
    n(int): n

returns:
    list: All primes till n
'''


def get_primes(n):
    prime_nums = [1, 2]
    even_nums = [x for x in range(3, n) if x % 2 != 0]

    for i in even_nums:
        root = int(ceil(sqrt(i))) + 1
        for j in range(3, root):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)

    print(prime_nums[0:n])


main()
