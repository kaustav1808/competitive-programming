__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

# Problem statement

# Sol - write down the solution in formal language
from typing import List

class solution:
    def quickSort(self,arr: List[int], startIndex: int, endIndex: int):
        if startIndex < endIndex:
            q = self.partition(arr, startIndex, endIndex)
            self.quickSort(arr, startIndex, q-1)
            self.quickSort(arr, q+1, endIndex)


    def partition(self,arr, start, end):
        key = start-1
        pivot = arr[end]
        j = start
        while (j <= end-1):
            if (arr[j] <= pivot):
                key += 1
                arr[j], arr[key] = arr[key], arr[j]
            j += 1
        arr[key+1], arr[end] = arr[end], arr[key+1]
        return key+1


def main():
    sol = solution()
    
    arr = [4, 3, 8, 4, 6, 5]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [5, 6, 7, 8]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [671, 541, 615, 637]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [760, 337, 720, 182, 724, 719, 278, 612, 647, 370, 216, 96, 36, 458, 532, 177]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [168, 486, 882, 519, 97, 114, 327, 564, 618, 834, 652, 224, 697, 742, 415, 828, 967, 800, 103, 353 ]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [871, 464, 718, 185, 816, 133, 604, 841, 349, 798, 960, 356, 449, 247, 710, 946, 872, 615, 936, 725, 622, 50, 609, 634, 131, 152, 900 ]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [96, 384, 667, 675, 523, 583, 895, 351, 525, 207, 137, 376, 99, 712, 526, 914, 36, 170, 731, 619, 10, 574, 900, 509]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [302, 401, 679, 712, 389, 377, 259, 605, 553, 467, 357, 998, 294, 369, 913, 932, 859, 324, 282, 161, 879, 344, 205, 988, 356]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)

    arr = [508, 418, 924, 517, 255, 939, 390, 627, 581, 728, 577, 389, 722, 26, 67, 950, 449, 477, 602, 702, 747, 882, 510, 699, 114]
    sol.quickSort(arr, 0,len(arr)-1)
    print(arr)
 


if __name__ == "__main__":
    main()
