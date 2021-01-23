if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = list(arr)

a = max(arr)
while max(arr) == a:
    arr.remove(max(arr))

print(max(arr))