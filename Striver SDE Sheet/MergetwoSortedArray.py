__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Given two sorted arrays, X[] and Y[] of size m and n each, 
# merge elements of X[] with elements of array Y[] by maintaining the sorted order, 
# i.e., fill X[] with the first m smallest elements and fill Y[] with remaining elements.

#Sol - we will use Gap method.

import math

class solution:
    def mergeTwoSortedArray(self,arr1,arr2):
        gap = self.nextGap(len(arr1) + len(arr2))
        while gap > 0:
            i = 0
            while i + gap < len(arr1):
                if arr1[i] > arr1[i+gap]: arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
                i += 1
            
            j = gap - len(arr1) if gap > len(arr1) else  0
            while i< len(arr1) and j < len(arr2):
                if arr1[i]>arr2[j]: arr1[i],arr2[j] = arr2[j], arr1[i]
                i += 1 
                j += 1

            if j < len(arr2):
                j = 0
                while j + gap < len(arr2):
                    if arr2[j] > arr2[j+gap]: arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                    j += 1      
            gap =  self.nextGap(gap)

        return arr1,arr2    

    def nextGap(self,gap):
        if gap == 1:return 0
        else: return math.ceil(gap/2)    


def main():
    mergeTwoSortedArray = solution()
    arr1, arr2 = mergeTwoSortedArray.mergeTwoSortedArray([3, 27, 38, 43],[9, 10, 82])
    print(arr1)     
    print(arr2)

    arr1, arr2 = mergeTwoSortedArray.mergeTwoSortedArray([2, 3, 8, 13], [1, 5, 9, 10, 15, 20])
    print(arr1)     
    print(arr2)     

if __name__ == "__main__":
    main()

