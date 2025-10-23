def find_max(nums):
   maximum_num = float("-inf")

   if len(nums) == 0:
      return None

   for num in nums:
      if num > maximum_num:
         maximum_num = num

   return maximum_num
