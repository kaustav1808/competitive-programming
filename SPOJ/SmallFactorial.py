def solveForN(fact):
    multiply = getRevDigit(fact)
    res = ''
    fact    -= 1
    while fact:
        if(fact>0):
            multiply = multiplyArray(multiply,fact)
        fact -=1
    multiply = reversed(multiply)
    for c in multiply:
        res += str(c)
    print(res,end="\n")    
 
def getRevDigit(num):
    digit = []
    while (num):
        digit.append(num%10)
        num = int(num/10)
    return digit

def multiplyArray(multiplicand,multiplier):
    carry = 0
    for i in range(0,len(multiplicand)):
        a = int(multiplicand[i] * multiplier) + carry
        multiplicand[i] = int(a%10)
        carry = int(a/10)
    if(carry):
        carry = getRevDigit(carry)
        for i in carry:
            multiplicand.append(int(i))
    return multiplicand        

t = int(input())
while t:
    t -=1
    n = int(input())
    solveForN(n)