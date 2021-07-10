# Solution
# 1. find Common Multiples of array a (Calculate LCM(Lowest Common Multiple)
# 2. find Common Divisors of array b (Calculate GCD(Greatest Common Divisor)
# 3. find Common Numbers between array a and b


def find_lcm(num1, num2):
    return int((num1 * num2) / find_gcd(num1, num2))


def find_gcd(num1, num2):
    while num1 * num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def getTotalX(a, b):
    rst, lcm, gcd = 0, a[0], 0

    for i in range(1, len(a)):
        lcm = find_lcm(lcm, a[i])
    for i in range(len(b)):
        gcd = find_gcd(gcd, b[i])

    num = lcm
    while num <= gcd:
        if gcd % num == 0: rst += 1
        num += lcm
    return rst


first_multiple_input = list(map(int, input().split()))
n, m = first_multiple_input[0], first_multiple_input[1]

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
result = getTotalX(arr, brr)
print(result)
