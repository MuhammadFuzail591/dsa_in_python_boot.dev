def quick_sort(nums, low, high):
   if low < high:
      middle_index = partition(nums, low, high)
      quick_sort(nums,low, middle_index - 1 )
      quick_sort(nums, middle_index + 1, high)


def partition(nums, low, high):
   pivot = nums[high]
   i = low - 1
   
   for j in range(low,high):
      if nums[j] <= pivot:
         i += 1
         nums[i],nums[j] = nums[j],nums[i]


   nums[i+1], nums[high] = nums[high], nums[i+1]

   return i+1