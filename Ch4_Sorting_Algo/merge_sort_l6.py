
def merge_sort(nums):
   
   if len(nums) < 2:
      return nums
   
   first_half = nums[:len(nums)//2]
   second_half = nums[len(nums)//2:]

   sorted_left_side = merge_sort(first_half)
   sorted_right_side = merge_sort(second_half)

   res = merge(sorted_left_side, sorted_right_side)

   return res


def merge(first, second):
   final = []
   i = 0
   j = 0

   while i < len(first) and j < len(second) :
      if first[i] <= second[j]:
         final.append(first[i])
         i +=1
      else:
         final.append(second[j])
         j += 1
   
   final.extend(first[i:])
   final.extend(second[j:])
   
   return final


