n = int(input())

if n == 1:
    print('Poor conductor')
    exit(0)

l = [(2, 3, 4, 5, 6), (11, 10, 9, 8, 7), (12, 13, 14, 15, 16), (21, 20, 19,
                                                                18, 17)]
# Seatinfo = namedtuple('Seatinfo', 'row_no position direction')

position = {0: ['W', 'L'], 1: ['A', 'L'], 2: ['A', 'R'], 3: ['M', 'R'],
            4: ['W', 'R']}

for row in l:
    for seat in row:
        if seat == n:
            print(l.index(row) + 1, end=' ')
            print('{} {}'.format(*position.get(row.index(seat),'Invalid')))
