__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

# Sol - write down the solution in formal language


class solution:
    def removeDuplicate(self,arr):
        if len(arr) < 2: return len(arr)
        i = 0
        j = 1

        while j < len(arr):
            if (arr[i] != arr[j]):
                i = j
                j += 1
            else:
                while j < len(arr) and arr[i] == arr[j]:
                    del arr[j]
        return len(arr)


def main():
    sol = solution()
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
    
    print(sol.removeDuplicate(arr))
    print(arr)


if __name__ == "__main__":
    main()
