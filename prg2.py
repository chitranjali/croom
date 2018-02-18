''' Prg-2'''
n = ' '
while n:
    n = int(input('enter a num'))
    res = 0
    if n % 3 == 0 and n % 5 == 0:
        res = 'both'
    elif n % 3 == 0:
        res = 'Three'
    elif n % 5 == 0:
        res = 'Five'


    print(res)
