def num_possible_orders(num_posts):
   
   factorial = 1

   for i in range(num_posts,0,-1):
      print(f"{i , factorial}")
      factorial *= i
   
   return factorial


res = num_possible_orders(564)/num_possible_orders(563)
print(res)