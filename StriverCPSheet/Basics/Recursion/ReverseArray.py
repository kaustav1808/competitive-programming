__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

#Sol - write down the solution in formal language

class solution:
    def reverseArray(self, arr ,start, end):
        if start<end: 
            arr[start], arr[end] = arr[end], arr[start]
            return self.reverseArray(arr, start+1, end-1)
        else: return arr


def main():
    sol = solution()
    arr = list(map(int,input().split(" ")))
    print(sol.reverseArray(arr,0,len(arr)-1))

if __name__ == "__main__":
    main()

