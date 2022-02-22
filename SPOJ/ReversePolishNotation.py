def solveRPN(ren):
    ren = list(ren)
    expr = ""
    stck = []
    operand = ['+','-','/','*','^']
    stck.append(ren.pop(0))

    while len(stck):
        pntr = ren.pop(0)

        if(pntr=='('):
            stck.append(pntr)
        elif pntr.isalpha():
            expr +=pntr 
        elif pntr in operand:
            stck.append(pntr)
        elif pntr==")":
            pntr = stck.pop()
            while pntr != "(":
                expr += pntr
                pntr = stck.pop()          
    
    print(expr,end="\n")




t = int(input())

while t:
    t -= 1
    rpn = input()
    solveRPN(rpn)