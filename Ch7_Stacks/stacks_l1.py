class Stack:
   def __init__(self):
      self.items = []

   def push(self, item):
      print(self.items)
      self.items.append(item)
      print(self.items)

   def size(self):
      return len(self.items)
