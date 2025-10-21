import math

def log_scale(data, base):
   
   logaritmic_list = []

   for entry in data:
      log = math.log(entry, base)
      logaritmic_list.append(log)

   return logaritmic_list

