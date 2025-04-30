
def bubbleSort(arr):
  n = len(arr)

  for i in range(n):
    isSwapped = False
    for j in range(n-1-i) :
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1] = arr[j+1] ,arr[j] 
        isSwapped = True
    
    if not isSwapped :
      break


arr = [3,2,4,1,5]
print("unsorted arr : ",arr)
bubbleSort(arr)
print("sorted arr : ",arr)

# did one mistake in first iteration