__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

#Sol - write down the solution in formal language


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxm = 0
        i = self.getFirstOne(0,nums)
        if i < 0: return maxm

        temp = i
        while i<len(nums):
            nums[i]
            if nums[i] == 1:
                maxm = max(maxm, i-temp+1)
                i += 1
            else:
                temp = self.getFirstOne(i+1, nums)
                if temp>0: 
                    i = temp
                else:
                    i = i + 1    
        return maxm            

    def getFirstOne(self, index, arr):
        if(index>=len(arr)): return -1
        if arr[index] == 1: return index
        for i in range(index, len(arr)): 
            if arr[i] == 1: 
                return i
        return -1


def main():
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([0,1]))

if __name__ == "__main__":
    main()

