__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Find out if a number is armstorng number or not

#Sol - take empty list and append all of the digit in the list. loop through the list and 
# take the power of len(list) of the digit and add in temp variable which is initialized to 0
# match the sum with the num and check equality

import math

class solution:
    def isArmstrong(self,num):
        tempNum = num
        temp = []
        tempSum = 0
        while(tempNum>0):
            dig = int(tempNum%10)
            temp.append(dig)
            tempNum = int(tempNum/10)

        for n in temp:
            tempSum += int(pow(n, len(temp)))     

        if tempSum == num : return True    
        else: return False    


def main():
    sol = solution()
    print("{num} is armstrong {isArmstrong}".format(num=0, isArmstrong=sol.isArmstrong(0)))
    print("{num} is armstrong {isArmstrong}".format(num=1, isArmstrong=sol.isArmstrong(1)))
    print("{num} is armstrong {isArmstrong}".format(num=2, isArmstrong=sol.isArmstrong(2)))
    print("{num} is armstrong {isArmstrong}".format(num=153, isArmstrong=sol.isArmstrong(153)))
    print("{num} is armstrong {isArmstrong}".format(num=152, isArmstrong=sol.isArmstrong(152)))
    print("{num} is armstrong {isArmstrong}".format(num=370, isArmstrong=sol.isArmstrong(370)))
    print("{num} is armstrong {isArmstrong}".format(num=371, isArmstrong=sol.isArmstrong(371)))
    print("{num} is armstrong {isArmstrong}".format(num=372, isArmstrong=sol.isArmstrong(372)))
    print("{num} is armstrong {isArmstrong}".format(num=407, isArmstrong=sol.isArmstrong(407)))
    print("{num} is armstrong {isArmstrong}".format(num=1634, isArmstrong=sol.isArmstrong(1634)))   
    print("{num} is armstrong {isArmstrong}".format(num=8208, isArmstrong=sol.isArmstrong(8208)))   

if __name__ == "__main__":
    main()

