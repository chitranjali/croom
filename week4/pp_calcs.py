sentinel = ''  # ends when this string is seen
tasks = []
op = ['+', '-', '*']
#  Loop over all input lines till blank line
for task in iter(input, sentinel):
    for i, ch in enumerate(task):
        if ch in op:
            tasks.append((task, ch, i,))


def add_sub(task):
    first_num = task[0][:task[2]]
    operator = task[0][task[2]]
    last_num = task[0][task[2] + 1:]
    len_f_num = len(str(first_num))
    len_l_num = len(str(last_num))
    length = len_f_num if len_f_num > len_l_num else len_l_num

    print(' ', first_num.rjust(length))
    print(operator,end='')
    print('', last_num.rjust(length))
    print('', '_' * (length + 1 ))
    print(' ', int(first_num) + int(last_num))


def mul(task):
    first_num = task[0][:task[2]]
    operator = task[0][task[2]]
    last_num = task[0][task[2] + 1:]
    len_f_num = len(str(first_num))
    len_l_num = len(str(last_num))
    length = len_f_num if len_f_num > len_l_num else len_l_num
    length = length + len_l_num

    print(' ', first_num.rjust(length))
    print(operator, end='')
    print('', last_num.rjust(length))
    print('', '_' * (length + 1))

    if len_l_num > 1:
        l = length
        for i in reversed(last_num):
                c = int(first_num)
                ind = str(int(c)*int(i))
                print(' ', ind.rjust(l))
                l = l - 1
        print('', '_' * (length + 1))

    print(' ', int(first_num) * int(last_num))
'''
Sample Input: 325*4405

Sample Output: 
    325
  *4405
  -----
   1625
     0
 1300
1300
-------
1431625
'''
if __name__ == '__main__':

    for task in tasks:
        if task[1] == '+' or task[1] == '-' :
            add_sub(task)
        elif task[1] == '*':
            mul(task)