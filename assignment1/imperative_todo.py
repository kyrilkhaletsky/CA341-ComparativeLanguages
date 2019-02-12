qu = [["11/11/17", "12:00", "01:30", ["Ashley", "John", "Sarah"]],
["15/11/17", "09:00", "Business Building"],
["16/11/17", "10:00", "Nursing Building"],
["11:00", "Science Building"],
["13/11/17", "13:00", "02:30", ["Benny", "Steve", "Bob", "Alan"]],
["17/11/17", "11:00", "Henry Grattan"],
["10/11/17", "10:00", "02:00", ["Mary", "John", "Scott"]],
["18/11/17", "12:00", "Computing Building"],
["12/11/17", "12:00", "03:00", ["Steve", "Mick"]],
["13/11/17", "18:00"]]

i = 0
for line in qu:
   length = 0
   for s in line:
      length = length + 1
   if length == 3:                                                                      #if length of line = 3, format it as an Event
      qu[i] = "Date: " + line[0] + ", Start Time: " + line[1] + ", Location: " + line[2]
      i+=1
   elif length == 4:                                                                    #if length of line = 4, format it as a Task   
      elem = ""
      for z in line[3]:
         elem = elem + "'" + z + "', "                              
      qu[i]= "Date: " + line[0] + ", Start Time: " + line[1] + ", Duration: " + line[2] + ", Assigned: [" + elem[:-2] + "]"
      i+=1
   else:
      qu = qu[:i] + qu[i+1:]
        													

#TEST
qu = qu[1:]                                                                             #remove top 2 items from the queue
qu = qu[1:]

while qu:                                                                               #while there are items in the queue
   print(qu[0])	                                                                        #       print the rest, top 2 items should not be printed
   qu = qu[1:]                                                                          #               as they have been removed from the queue earlier
       
