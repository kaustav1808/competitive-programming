__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Find out if a string is a palindrome or not using recursion

#Sol - write a recursion function ispalindrome(arr, start, end)

class solution:
    def isPalindrome(self, arr, start, end):
        if start < end: 
            if arr[start] == arr[end]: return self.isPalindrome(arr, start+1, end-1)
            else: return False
        else: return True    


def main():
    sol = solution()
    arr = input()
    print(sol.isPalindrome(arr,0,len(arr)-1))   

if __name__ == "__main__":
    main()

