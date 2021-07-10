def timeConversion(s):
    if s[:2] == '12':
        if s[-2:] == 'AM':
            s = s.replace(s[:2], '00')
    elif s[-2:] == 'PM':
        s = s.replace(s[:2], str(int(s[:2]) + 12))
    return s[:-2]


s = input()
rst = timeConversion(s)
print(rst)