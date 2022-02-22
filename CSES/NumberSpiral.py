t = int(input())


def solve(y, x):
    z = max(y, x)
    ap = z * (z-1)+1
    if z % 2:
        print(ap+x-y)
    else:
        print(ap+y-x)


while (t > 0):
    y, x = map(int, input().split())
    solve(y, x)
    t -= 1
