

# In each pass, compare adjacent elements.
# Swap if they're in the wrong order.
# After each pass, the largest element bubbles to the end.

def bubble_sort(arr):
  n=len(arr)
  for i in range(n):
    for j in range(n-1-i):
      if(arr[j]>arr[j+1]):
        arr[j] , arr[j+1] = arr[j+1], arr[j]


arr = [3,2,4,1,5]
print("unsorted",arr)
bubble_sort(arr)
print("sorted",arr)
