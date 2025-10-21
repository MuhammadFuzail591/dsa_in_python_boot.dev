def average_followers(nums):
   if len(nums) == 0:
      return None

   sum_of_nums = 0
   total_numbers_in_list = len(nums)

   for i in nums:
      sum_of_nums += i


   average = sum_of_nums / total_numbers_in_list

   return average

