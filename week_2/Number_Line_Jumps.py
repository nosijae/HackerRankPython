# 어거지로 끼워 맞춤, 굉장히 안좋은 답안

def kangaroo(x1, v1, x2, v2):
    rst = 'No'
    while True:
        if v2 > v1 or x1 > x2: break
        if x1 != x2 and v1 == v2: break
        if x1 == x2:
            rst = 'Yes'
            break
        x1 += v1
        x2 += v2
    return rst


first_multiple_input = list(map(int, input().split()))
x1, v1, x2, v2 = first_multiple_input[0], first_multiple_input[1], first_multiple_input[2], first_multiple_input[3]
result = kangaroo(x1, v1, x2, v2)
print(result)
