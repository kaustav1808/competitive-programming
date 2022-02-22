n = int(input())

while n:
    n -= 1
    s = input()
    if len(s) > 10:
        s = s[0]+str(len(s[1:len(s)-1]))+s[-1:]
        print(s)
    else:
        print(s)
