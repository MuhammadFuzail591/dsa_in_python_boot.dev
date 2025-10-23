def binary_search(target, arr):
   low = 0
   list_length = len(arr)
   high = list_length - 1


   while low <= high:
      median = (low + high) // 2

      if arr[median] == target: return True
      elif arr[median] < target: low = median + 1
      else: high = median - 1

   return False
