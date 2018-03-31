import itertools

s = input()
no = 0
for i in range(1, len(s) + 1):
    sub_s = itertools.permutations(s,i)
    non_rep = set(sub_s)
    for i, sub in enumerate(non_rep):
        print(no, sub)
        no = no + 1
print()
print()
print()
print()

no = 0
for i in range(1, len(s) + 1):
    sub_s = itertools.combinations(s,i)
    non_rep = set(sub_s)
    for i, sub in enumerate(non_rep):
        print(no, sub)
        no = no + 1