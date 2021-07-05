def plusMinus(arr):
    n = len(arr)
    pst = 0
    ngt = 0
    zr = 0

    for i in arr:
        if i < 0:
            ngt += 1
        elif i == 0:
            zr += 1
        else:
            pst += 1

    a, b = pst / n, ngt / n
    c = 1 - a - b
    print('%.6f\n%.6f\n%.6f' %(a, b, c))

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
