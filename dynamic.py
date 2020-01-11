import math, threading, time

time_period = 3600	#In seconds, can be reduced.
next_call = time.time()
new_list = None, old_list = None	#Read from text file?


def analysis(new_list = None, old_list = None, next_call = 3601):
  while (next_call - time.time() < 0):
    #THING HERE

#FIND A MIDDLE-GROUND FOR THE THREADING PART OF THE PROJECT

def check(new_list = None, old_list = None, next_call = 3601):
  while (next_call - time.time() < 0):
    
#ROUGH CODE TO SPLIT THE IP ADDRESS. FIGURE OUT HOW TO PASS IT TO A C++ PROGRAM
	print ip
	x = ip.split(".")

	#USE THIS FOR FURTHER CHANGES. MAYBE CONVERT TO INT ARRAY HERE?
	filename = x[1]
	filename = filename[1:]


def kNN(points, p, k = 3):

	distance = [] 
	for group in points: 
		for feature in points[group]: 
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 
			distance.append((euclidean_distance, group)) 

	distance = sorted(distance)[:k] 

	type1 = 0
	type2 = 0

	for d in distance: 
		if d[1] == 0: 
			type1 += 1
		elif d[1] == 1: 
			type2 += 1

	return 0 if type1 > type2 else 1



def launch():


