q = int(input())

def smallestChefora(num):
    b = str(num//10)
    if int(b):b = str(num)+b[::-1]
    else:b=num
    return int(b)

def solve():
    l,r = map(int,input().split())
    i = 1
    m = 1000000007
    al = smallestChefora(l)
    for j in range(l+1,r+1):
        i = (i * (al**smallestChefora(j))) % m
    print(i)    


while q:
    solve()
    q -= 1