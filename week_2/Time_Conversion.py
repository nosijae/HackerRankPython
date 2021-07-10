def timeConversion(s):
    arr = s.split(':')

    if 'PM' in arr[-1] and int(arr[0]) < 12:
        arr[0] = int(arr[0]) + 12
        arr[0] = str(arr[0])
    elif 'AM' in arr[-1] and int(arr[0]) >= 12:
        arr[0] = int(arr[0]) - 12
        arr[0] = str(arr[0])
    if len(arr[0]) < 2:
        arr[0] = '0' + arr[0]

    arr[-1] = arr[-1][:2]
    s = ':'.join(arr)
    return s


s = input()
print(timeConversion(s))