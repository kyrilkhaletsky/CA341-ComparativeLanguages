from Queue import Queue
import os

class Task():
   def __init__(self, date, start_time, duration, people=[]):
      self.date = date
      self.start = start_time
      self.duration = duration
      self.people = people
      
   def __str__(self):
      return "Date: {}, Beginning: {}, Duration: {}, Attending: {}".format(self.date, self.start, self.duration, self.people)
      
   def __repr__(self):
      return str(self)    
   
class Event():
   def __init__(self, date, start_time, location):
      self.date = date
      self.start = start_time
      self.location = location
   
   def __str__(self):     
      return "Date: {}, Beginning: {}, Location: {}".format(self.date, self.start, self.location)
      
class Todo():

   def __init__(self, q):
      self.q = q
    
   def add_item(self, item): 
      self.q.put(item)
      
   def remove_item(self):
      return self.q.get()
   
def test():
   q = Queue()

   l = Todo(q)
   l.add_item(Task("21/07/17", 1600, 60, ["George", "Micheal", "Anna", "Edd"]))
   l.add_item(Event("05/03/18", 1200, "My House"))
   l.add_item(Task("11/06/18", 1100, 120, ["Micheal, Anna"]))
   l.add_item(Task("20/01/18", 1700, 30, ["George", "Micheal", "Edd"]))
   l.add_item(Event("07/03/18", 1300, "Your House"))
   
   while not q.empty():
      print(l.remove_item())
   rows, columns = os.popen('stty size', 'r').read().split() 
   print("-----")
   
   l.add_item(Task("21/07/17", 1600, 60, ["George", "Micheal", "Anna", "Edd"]))
   l.add_item(Event("05/03/18", 1200, "My House"))
   print(l.remove_item())
   l.add_item(Task("11/06/18", 1100, 120, ["Micheal, Anna"]))
   l.add_item(Task("20/01/18", 1700, 30, ["George", "Micheal", "Edd"]))
   print(l.remove_item())
   l.add_item(Event("07/03/18", 1300, "Your House"))
      
def main():
   test() 
     
if __name__ == "__main__":
   main()
