class Stack:
   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.append(item)

   def size(self):
      return len(self.items)

   def peek(self):
      if self.items == []:
         return None
      peek_element = self.items[-1]
      return peek_element

   def pop(self):
      if self.items == []:
         return None
      
      return self.items.pop()
