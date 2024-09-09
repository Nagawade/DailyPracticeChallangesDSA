arr = [0,1,2,1,0,2,1,0]
def partation(low,high):
    pivot = arr[low]
    i = low
    j = high

    while(i<j):
        while( i <= high and arr[i]<=pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def QuickSort(low,high):
    if(low<high):
        j = partation(low,high)
        QuickSort(low,j-1)
        QuickSort(j+1,high)


QuickSort(0,len(arr)-1)
print(arr)