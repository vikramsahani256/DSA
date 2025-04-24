
# find the min in 1 loop then swap it with ith index
# select the min and arrange on 1st place of the array


def selection_sort(arr,n):
  for i in range(n):
    min_ind = i
    
    for j in range(i+1, n):
      if(arr[min_ind]>arr[j]):
        min_ind = j

    arr[min_ind], arr[i] = arr[i] , arr[min_ind]


arr = [3,2,4,1,5]
print("unsorted",arr)
n =  len(arr)
selection_sort(arr,n)
print("sorted",arr)
