def quickSort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]
    left, right = start + 1, end

    while left <= right:
        while left <= end and arr[left] < pivot:
            left += 1
        while right >= start and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr[start], arr[right] = arr[right], arr[start]
    quickSort(arr, start, right)
    quickSort(arr, right + 1, end)

arr = list(map(int, input().split()))
quickSort(arr, 0, len(arr) - 1)
print(arr)
