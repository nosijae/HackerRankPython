def diagonalDifference(arr):
    rst = 0
    i = 0
    while True:
        if i == len(arr):
            return abs(rst)
        rst += arr[i][i] - arr[i][len(arr) - 1 - i]
        i += 1


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)
