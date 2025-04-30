

def merge(left, right):

  res = []
  l = r = 0
  while(l<len(left) and r < len(right)):
    if left[l] < right[r] :
      res.append(left[l])
      l+=1
    else :
      res.append(right[r])
      r+=1

  while(l<len(left)):
    res.append(left[l])
    l+=1

  while(r<len(right)):
    res.append(right[r])
    r+=1

  return res

def mergeSort(arr):

  if(len(arr) == 1):
    return arr
  
  mid = len(arr) // 2

  left  = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left, right)




arr = [3,2,4,1,5]
print("unsorted arr : ",arr)
arr = mergeSort(arr)
print("sorted arr : ",arr)

"""
mistakes :
1.   return merge(left, right) -> 34
2.   arr = mergeSort(arr) -> 41

"""