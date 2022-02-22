import math
n = int(input())
seq = list(map(int, input().split()))
tot = 0
prev = seq[0]

for i in range(1, n):
    tot += max(0, prev - seq[i])
    prev = max(prev, seq[i])

print(tot)
