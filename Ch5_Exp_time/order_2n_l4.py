def power_set(input):
   if len(input) == 0:
      return [[]]
   
   all_subsets = [[]]

   for element in input:
      new_subsets = []
      for each_subset in all_subsets:
         new_subsets.append(each_subset + [element])
      all_subsets.extend(new_subsets)

   return all_subsets


