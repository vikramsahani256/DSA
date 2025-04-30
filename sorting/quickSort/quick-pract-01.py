

def partition(arr, low, high):

  pivot = arr[high]
  i = low - 1

  for j in range(low , high):
    if(arr[j]<pivot):
      i+=1
      arr[i], arr[j] = arr[j],arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1 # current pivot position



def quickSort(arr,low,high) :
  
  if low < high :
    pi = partition(arr, low, high)

    quickSort(arr, low, pi -1 )
    quickSort(arr, pi + 1, high )



arr = [3,2,4,1,5]
print("unsorted arr : ",arr)
low = 0
high = len(arr) - 1
quickSort(arr, low, high)
print("sorted arr : ",arr)