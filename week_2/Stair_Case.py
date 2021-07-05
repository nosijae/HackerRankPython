def staircase(n):
    for i in range(n):
        print(' ' * (n - i - 1), end= '')
        print('#' * (i + 1))

n = int(input())
staircase(n)