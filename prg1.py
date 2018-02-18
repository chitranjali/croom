''' Remove duplicates from list(order matters)'''

from collections import OrderedDict, defaultdict
l1 = [1, 2, 3, 4, 5, 5, 6, 13, 13, 9]

l1_uniq = list(OrderedDict.fromkeys(l1))
print(l1_uniq)

