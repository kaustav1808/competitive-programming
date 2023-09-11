__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Find out all Divisors of a given Number

#Sol - take square root of the number n and through the square root of the number 
# if i in loop divide the number then print i also if (i!=n/i) print n/i 
# as n/i is also the divisor of the number

import math

class solution:
    def divisors(self,num):
        for i in range(0, int(math.sqrt(num))+1):
            if(i==0):continue
            if(num%i==0):
                print(i)
                if(i!=num/i): print(num/i)    


def main():
    sol = solution()
    for i in range (1,51):
        print("--------------------------------")
        print("{num} divisors is".format(num=i))
        sol.divisors(i)
        print("--------------------------------")
     

if __name__ == "__main__":
    main()

