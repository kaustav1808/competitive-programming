__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

#Sol - write down the solution in formal language

class solution:
    def factorial(self, n):
        if n==1: return 1
        else: return n * self.factorial(n-1)


def main():
    print("enter -1 to exit")
    num = int(input())
    sol = solution()

    while num>0:
        print("factorial of {num} is {factorial}".format(num=num,factorial=sol.factorial(num)))
        print("enter -1 to exit")
        num = int(input())

if __name__ == "__main__":
    main()

