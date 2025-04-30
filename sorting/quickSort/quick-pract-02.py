

def partion(arr,low,high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if(arr[j]<pivot):
      i+=1
      arr[j] , arr[i] = arr[i] , arr[j]

  arr[i+1] , arr[high] = arr[high] , arr[i+1]

  return i+1 


def quickSort(arr,low, high):
  if low < high :
    pi = partion(arr, low, high)
    quickSort(arr, low,  pi-1)
    quickSort(arr,   pi+1, high)


arr = [3,4,1,2,2,6,8,7]
print("unsorted Arr : ", arr)
quickSort(arr,0,len(arr)-1)
print("sorted Arr : ", arr)