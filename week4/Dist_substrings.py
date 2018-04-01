'''
Given a string, we need to find the total number of its distinct substrings.
'''
s = input()
no = 0
l = []

for i in range(1, len(s) + 1):
    for j in range(0, i):
        sub = s[j:i]
        if sub not in l:
            l.append(sub)

print(len(l))