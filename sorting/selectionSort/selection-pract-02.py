def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1,n):
      if(arr[min_index]>arr[j]) :
        min_index = j
    arr[min_index] , arr[i] = arr[i], arr[min_index]



arr = [3,2,4,1,5]
print("orginal arr : ",arr)
selectionSort(arr)
print("sorted arr : ",arr)
