'''快速排序算法实现
时间复杂度O(nlog2n)
'''

def QuickSort(arr, FirstIndex, LastIndex):

    if FirstIndex == LastIndex:
        return
    if FirstIndex < LastIndex:
        divIndex = Partition(arr, FirstIndex, LastIndex)

    if divIndex > FirstIndex:
        QuickSort(arr, FirstIndex, divIndex-1)
    if divIndex < LastIndex:
        QuickSort(arr, divIndex+1, LastIndex)

def Partition(arr, FirstIndex, LastIndex):
    i = FirstIndex - 1
    for j in range(FirstIndex, LastIndex):
        if arr[j] <= arr[ LastIndex]:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[LastIndex] = arr[LastIndex], arr[i]
    return i

if __name__ == '__main__':
    arr = [1,4,7,1,5,5,3,85,34,75,23,75,2,0]
    print("initial array:\n", arr)
    QuickSort(arr, 0, len(arr)-1)
    print("after quicksort:\n", arr)
