l = [1, [1,8,[5,6],0],9]
# l = [1, [1,8],9]
new_list = []

def make_list(l):
    for item in l:
        if isinstance(item, list):
            make_list(item)
        else:
            new_list.append(item)

    return new_list

make_list(l)
print(new_list)

