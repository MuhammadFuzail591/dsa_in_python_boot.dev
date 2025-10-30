class Queue:
   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.insert(0, item)

   def pop(self):
      if self.items == []:
         return None
      
      return self.items.pop()

   def peek(self):
      if self.items == []:
         return None
      element = self.items[-1]
      return element

   def size(self):
      number_of_items = len(self.items)
      return number_of_items
