def solveForN(n,m):
    n = addArray(getRevDigit(m),getRevDigit(n))    
    res = ''
    for c in n:
        res += str(c)
    print(res.lstrip("0"),end="\n")    
 
def getRevDigit(num):
    digit = []
    while (num):
        digit.append(num%10)
        num = int(num/10)
    return digit

def addArray(adder,addend):
    carry = 0
    res   = []
    while len(adder) or len(addend):
        if len(adder):
            a = adder.pop()
        else:
            a = 0

        if len(addend):
            b = addend.pop()
        else:
            b = 0
        res.append(int((a+b+carry)%10))
        carry = int((a+b+carry) / 10)
    if carry:
        res.append(carry)
    return res           
         
t = int(input())
while t:
    t -=1
    n,m = map(int,input().split(" "))
    solveForN(n,m)