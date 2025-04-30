def insertionSort(arr):
  n = len(arr) 
  for i in range(1, n):

    min_card = arr[i]
    j = i - 1
    
    while j>= 0 and arr[j] > min_card :
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = min_card 


arr = [3,2,4,1,5]
print("unsorted arr : ", arr)
insertionSort(arr)
print("sorted arr : ", arr)

#did on mistake in first iteration