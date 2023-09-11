__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# find out n fibonacci numbers using recursion

#Sol - write a recursion function fibonacci(n)

class solution:
    def fibonacci(self, num):
        if num==0: return 0
        elif num==1: return 1
        else: 
            return self.fibonacci(num-1) + self.fibonacci(num-2)


def main():
    sol = solution()
    num = int(input())
    print("{n} fibonacci numbers is {fibonacci}".format(n=num,fibonacci=sol.fibonacci(num))) 

if __name__ == "__main__":
    main()

