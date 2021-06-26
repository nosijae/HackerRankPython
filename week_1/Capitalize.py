def solve(s):
    str_list = s.split(' ')
    rst = ''
    for i in str_list:
        if i == '':
            rst += ' '
            continue
        rst += i[0].upper() + i[1:]
        rst += ' '
    return rst

s = input()
result = solve(s)
print(result)