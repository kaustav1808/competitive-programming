class solution:
    def moveNegative(self, arr):
        i = 0
        j = len(arr) - 1

        while i < j:
            if (arr[i] < 0) and (arr[j] < 0): 
                i += 1
                continue
            elif (arr[i] > 0) and (arr[j] > 0): 
                j -=1
                continue
            elif (arr[i]>0) and (arr[j]<0): 
                arr[i], arr[j] = arr[j], arr[i]
            i += 1     
            j -= 1

if __name__=='__main__':
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    sol = solution()
    sol.moveNegative(arr)
    print(arr)                 