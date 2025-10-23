# def find_last_name(names_dict, first_name):
#    for current_first_name, last_name in names_dict.items():
#       if current_first_name == first_name:
#          return last_name


def find_last_name(names_dict, first_name):
   try:
      last_name = names_dict[first_name]
      return last_name
   except KeyError:
      print("Key is not found..!!")
      return None