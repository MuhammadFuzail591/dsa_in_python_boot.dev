def exponential_growth(n, factor, days):
   
   growth_sequence = [n]

   i = 1
   value = n

   while i < days + 1:
      value *= factor
      growth_sequence.append(value)
      i += 1

   print(growth_sequence)
   return growth_sequence


exponential_growth(10,2,4)

   
