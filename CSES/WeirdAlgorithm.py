n = int(input())

while n > 0:
    print(n)
    if n == 1:
        break
    elif not n % 2:
        n //= 2
    else:
        n *= 3
        n += 1
