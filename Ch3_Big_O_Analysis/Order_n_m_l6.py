def get_avg_brand_followers(all_handles, brand_name):

   if len(all_handles) == 0:
      return None
   
   num_of_lists = len(all_handles)
   num_of_handles = 0

   for handle_list in all_handles:
      for handle in handle_list:
         if brand_name in handle:
            num_of_handles += 1

   res = (num_of_handles / num_of_lists)
   return round(res,2)

