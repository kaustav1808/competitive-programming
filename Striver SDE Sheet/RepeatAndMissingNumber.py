__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Given an unsorted array of size n. Array elements are in the range from 1 to n. 
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
#  Find these two numbers..

#Sol - using an index array, we set all position with -1. Iterate the main array, and increment the 
#      positon of index array by 1. Then we again iterate, if a negative number found it will be missing.
#      if a positive number found it will be repeated number.
#      time complexity o(2n), space complexity o(n). 


from typing import List


class solution:
    def findMissingRepitingNumber(self, nums:List[int]) ->None:
        arr = [-1 for _ in range(len(nums)+1)]
        for each in range(len(nums)):
            arr[nums[each]] += 1
        missing = []
        repeat  = []

        for each in range(1,len(arr)):
            if arr[each] < 0:
                missing.append(each)
            if arr[each] > 0:
                repeat.append(each)

        print("missings numbers are {a}".format(a=",".join(str(v) for v in missing)))                 
        print("repeated numbers are {a}".format(a=",".join(str(v) for v in repeat)))   


def main():
    findMissingAndRepeatedNumbers = solution()
    findMissingAndRepeatedNumbers.findMissingRepitingNumber([1,2,3,8,9,8,6,3,5])     

if __name__ == "__main__":
    main()                       
