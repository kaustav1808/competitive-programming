__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Sort an array of 0’s 1’s 2’s without using extra space

#Sol - using couting sort, we count the number of 0's, 1's, 2's in the nums.
#      After we modify the array with appropriate no of 0's, 1's and 2's.

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_no = [0,0,0]
        for i in nums:
            count_no[i] += 1
        
        for i in range(len(nums)):
            while count_no[0]:
                nums[i]      = 0
                count_no[0] -= 1
                i += 1 
            while count_no[1]:
                nums[i]      = 1
                count_no[1] -= 1
                i += 1
            while count_no[2]:
                nums[i]      = 2
                count_no[2] -= 1
                i += 1