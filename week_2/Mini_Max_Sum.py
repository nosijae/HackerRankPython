
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:len(arr) - 1]), sum(arr[1:]))


arr = list(map(int, input().split()))
miniMaxSum(arr)