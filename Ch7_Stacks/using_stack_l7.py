
from stack import Stack


def is_balanced(input_str):
   new_stack = Stack()

   for character in input_str:
      if character == "(":
         new_stack.push(character)
      if character == ")":

         if new_stack.is_empty():
            return False
         new_stack.pop()
         
      
   return new_stack.is_empty()


value = is_balanced("()(()))")
print(value)