def get_estimated_spread(audiences_followers):

   num_of_followers = len(audiences_followers)
   if num_of_followers == 0:
      return 0

   sum_of_followers = 0

   for follower in audiences_followers:
      sum_of_followers += follower

   average_audience_followers = sum_of_followers / len(audiences_followers)

   print(audiences_followers, sum_of_followers, average_audience_followers)

   estimated_spread = average_audience_followers * ( num_of_followers ** 1.2 )

   return estimated_spread

