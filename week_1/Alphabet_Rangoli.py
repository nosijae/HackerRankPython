def print_rangoli(size):
    # your code goes here
    alpha = list(chr(i) for i in range(97, 123))

    for i in range(1, size * 2):
        print(
            '--' * abs(size - i) + '-'.join(alpha[size - 1:abs(size - i):-1] + alpha[abs(size - i):size]) + '--' * abs(
                size - i))


size = int(input())
print_rangoli(size)
