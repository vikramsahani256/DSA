

def merge(left , right):

  i = j  = 0
  res = []

  while i< len(left)  and j < len(right) : 
    if left[i] < right[j] :
      res.append(left[i])
      i+=1
    else :
      res.append(right[j])
      j+=1

  while i< len(left) : 
    res.append(left[i])
    i+=1

  while j< len(right) : 
    res.append(right[j])
    j+=1
  return res



def mergeSort(arr):
  if len(arr) == 1 :
    return arr
  
  mid = len(arr)//2

  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left,right)



arr = [3,4,1,2,6,8,7]
print("unsorted Arr : ", arr)
arr = mergeSort(arr)
print("sorted Arr : ", arr)