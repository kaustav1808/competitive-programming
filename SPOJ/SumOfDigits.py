def sumOfDigits(num):
    if not(num // 10):
        return (num*(num+1))/2

    n = str(num)
    n = len(n)
    first = num // pow(10, n-1)
    sum = 0
    pos_sum = pow(10, n-2) * 45 * (n-1)
    for i in range(first):
        sum += i * pow(10, n-1) + pos_sum
    sum += first*(num % pow(10, n-1)+1)
    return sum + sumOfDigits(num % pow(10, n-1))


while True:
    a, b = map(int, input().split(" "))
    if(a != -1) and (b != -1):
        print(int(sumOfDigits(b))-int(sumOfDigits(a-1)))
    else:
        break
