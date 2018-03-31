def get_near_pali(num_list, near_num, half):

    if num_list >= near_num:
        if near_num[(half)] != 9:
            near_num[(half)] = near_num[(-(half + 1))] = near_num[(half)] + 1
        else:
            near_num[(half)] = near_num[(-(half + 1))] = 0
            half -= 1
        half -= 1
        return get_near_pali(num_list, near_num, half)
        print(near_num)
    else:
        return near_num

if __name__ == '__main__':
    num_list = list(map(int,input()))
    near_num = num_list.copy()

    half = int(len(num_list) / 2)

    for index, item in enumerate(num_list[:half]):
        near_num[-(index + 1)] = near_num[(index)] = item

    ans = get_near_pali(num_list,near_num,half)
    print(''.join(map(str,ans)))
