def selectionSort(arr):
  n = len(arr) 
  for i in range(n):
    minIndex = i
    for j in range(i,n):
      if(arr[j] < arr[minIndex]) :
        minIndex = j
    arr[minIndex], arr[i] = arr[i] , arr[minIndex]


arr = [3,4,1,2,2,6,8,7]
print("unsorted Arr : ", arr)
selectionSort(arr)
print("sorted Arr : ", arr)