def count_names(list_of_lists, target_name):
   
   count = 0

   if len(list_of_lists) == 0:
      return 0
   
   for outer_list in list_of_lists:
      for name in outer_list:
         if name == target_name:
            count += 1
   
   return count
