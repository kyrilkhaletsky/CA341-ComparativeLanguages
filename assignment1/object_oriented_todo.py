class Queue:                                                                    #my implementation of a queue
    def __init__(self):
        self.items = []

    def isEmpty(self):                                                          #checks if a queue is empty
        return self.items == []

    def enqueue(self, item):                                                    #adds an item to a queue
        self.items.insert(0,item)

    def dequeue(self):                                                          #deletes an item from a queue
        return self.items.pop()

		
class Event():                                                                  #event class, takes in a list and returns
   def __init__(self, line):                                                    #a formatted string with date, start and location
      self.date = line[0]
      self.start = line[1]
      self.location = line[2]
   
   def __str__(self):     
      return "Date: {}, Start Time: {}, Location: {}".format(self.date, self.start, self.location)


class Task():                                                                   #task class, takes in a list and returns
   def __init__(self, line):                                                    #       a formatted string with date, start, duration, a list of people
      self.date = line[0]
      self.start = line[1]
      self.duration = line[2]
      self.people = line[3]
      
   def __str__(self):
      return "Date: {}, Start Time: {}, Duration: {}, Assigned: {}".format(self.date, self.start, self.duration, self.people)
	  
	  
class ToDo():                                                                   #my ToDo queue class
   def __init__(self, queue):
      self.queue = queue
    
   def add_item(self, item):                                                    #adds an item to a queue
      self.queue.enqueue(item)
      
   def remove_item(self):                                                       #removes an item from a queue
      return self.queue.dequeue()
       

def InOut(act):                                                                 #test the queue
   queue = Queue()
   td = ToDo(queue)

   for line in act:                                                             #act contains the tasks and events
      if len(line) == 3:                                                        #if its an Event
         td.add_item(Event(line))                                               #       Add that item to a queue & format it with the Event class
      else:                                                                     #if its a Task
         td.add_item(Task(line))                                                #       Add that item to a queue & format it with the Task class

#TEST
   td.remove_item()                                                             #remove the top 2 items from the queue
   td.remove_item()

   while not queue.isEmpty():                                                   #while there are items in the queue
      print(td.remove_item())                                                   #       print the rest, top 2 items should not be printed
                                                                                #               as they have been removed from the queue earlier

def main():

   infile = open('todo.txt').read().splitlines()                                #read in a set of tasks/events from a text file
   act = []
   
   for line in infile:												
      line_list = line.split(', ', maxsplit=3)                                  #split each line by a comma ", "
      if len(line_list) == 4:										
         line_list[3] = line_list[3].strip("[]").split(', ')                    #if the length is 4 its an event, convert people into a list
         act.append(line_list)										
      elif len(line_list) == 3:                                                 #if the length is 3 its a task
         act.append(line_list)                                                  #append both onto a list
      else:                                                                     #if length != 3 or 4 then skip, its invalid
         continue
   
   InOut(act)                                                                   #run the test

     
if __name__ == "__main__":
   main()

