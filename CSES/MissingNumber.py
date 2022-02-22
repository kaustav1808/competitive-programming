n = int(input())
m = map(int, input().split())
s = 0
for i in m:
    s += i

n = (n * (n+1)) // 2
print(n-s)
