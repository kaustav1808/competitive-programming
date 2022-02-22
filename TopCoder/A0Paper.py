class A0Paper:
    def canBuild(self, A):
        if(A[0]==1):
            return "Possible"
        key = 1
        
        multiplier = 2
        currentCost = 0
        for key in range(len(A)):
            if (A[key]/multiplier):
                return "Possible"
            elif (currentCost+(A[key]/(multiplier/2))) ==1:
                return "Possible"
            else:
                multiplier *= 2
                currentCost += (A[key]/(multiplier/2))
        return "Impossible"        