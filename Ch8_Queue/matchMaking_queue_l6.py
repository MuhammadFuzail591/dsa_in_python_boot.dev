
from queue_class import Queue


def matchmake(queue, user):
   action = user[1]
   print(action)
   if action == 'leave':
      queue.search_and_remove(user[0])
   if action == 'join':
      queue.push(user[0])

   if len(queue.items) >= 4:
      
      user1 = queue.pop()
      user2 = queue.pop()

      return f'{user1} matched {user2}!'
   else:
      return "No match found"
