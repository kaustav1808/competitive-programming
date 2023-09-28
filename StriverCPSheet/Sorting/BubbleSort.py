__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

#Sol - write down the solution in formal language

class solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]
        return arr                    


def main():
    sol = solution()
    arr = list(map(int,input().split(" ")))
    print("{arr} after sorted {sorted}".format(arr=arr,sorted=sol.bubbleSort(arr)))

if __name__ == "__main__":
    main()