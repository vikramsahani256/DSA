
def insertion_sort(arr):
  n = len(arr)

  for i in range(1,n):
    
    card = arr[i] # choosen a card
    j = i-1 

    while j>=0 and arr[j] > card :
      arr[j+1] = arr[j] 
      j-=1

    arr[j+1] = card
    

arr = [3,2,4,1,5]
print("unsorted Arr : ",arr)
insertion_sort(arr)
print("sorted Arr : ",arr)