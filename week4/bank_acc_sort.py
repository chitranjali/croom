from collections import Counter
'''
Sort account numbers in order and repetitions

Input case 1
03 10103538 2222 1233 6160 0142 
03 10103538 2222 1233 6160 0141 
30 10103538 2222 1233 6160 0141 
30 10103538 2222 1233 6160 0142 
30 10103538 2222 1233 6160 0141 
30 10103538 2222 1233 6160 0142 

Output 
03 10103538 2222 1233 6160 0141 1
03 10103538 2222 1233 6160 0142 1
30 10103538 2222 1233 6160 0141 2
30 10103538 2222 1233 6160 0142 2

'''
sentinel = ''  # ends when this string is seen
acc_nos = []

#  Loop over all input lines till blank line
for ac in iter(input, sentinel):
    acc_nos.append(int(ac.replace(' ', '')))

acc_nos.sort()
coun = Counter(acc_nos)
for key, value in sorted(coun.items()):
    ac = str(key)
    if len(ac) < 26:
        ac = ac.zfill(26)
    print('{} {} {} {} {} {} {}'.format(ac[0:2], ac[2:10], ac[10:14], ac[14:18], ac[18:22], ac[22:27], value))
