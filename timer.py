import math, threading, time

time_period = 3600	#In seconds, can be reduced.
next_call = time.time()
new_list = None, old_list = None	#Read from text file.
#IP addresses = device ID -> You can assume less than 255 entries.


def security_analysis():
  global next_call, new_list
  next_call = next_call + time_period
  if (new_list is None):
    #Write previous data to something before it gets overwritten

  #Create new dataset over here!
  threading.Timer(next_call - time.time(), foo).start()


def security_check():
  global next_call, finished_list
  next_call = next_call + time_period
  if(old_list is None):
    threading.Timer(next_call - time.time(), foo).start()

def manager():
  ababa
