def mergeSort(arr: [int], l: int, r: int):
    if l >= r: return
    mid = int((l+r)/2)
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr, l, mid ,r):
    temp = list()
    left = l
    right = mid + 1
    
    while left <= mid and right<= r:
        if (arr[left] <= arr[right]): 
            temp.append(arr[left])
            left += 1
        elif (arr[left] > arr[right]):
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= r:
        temp.append(arr[right])
        right += 1    

    for i in range(l,r+1): arr[i] = temp[i-l]

def main():
    arr = list(map(int,input().split(" ")))
    print("{arr} after sorted {sorted}".format(arr=arr,sorted=mergeSort(arr,0,len(arr)-1)))

if __name__ == "__main__":
    main()