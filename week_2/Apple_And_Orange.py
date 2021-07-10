def countApplesAndOranges(s, t, a, b, apples, oranges):
    rst1, rst2 = 0, 0

    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            rst1 += 1
    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            rst2 += 1

    print(rst1)
    print(rst2)


first_multiple_input = input().rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
