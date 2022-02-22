import math

m, n = map(int, input().split())

if m % 2:
    print(math.floor(m/2)*n+math.floor(n/2))
else:
    print(math.floor(m/2)*n)
