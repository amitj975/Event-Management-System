from hopcroftkarp import HopcroftKarp
from .models import Profile, Event

#graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6},'g': {5, 6, 7}, 'h': {8}}



# HopcroftKarp(graph).maximum_matching()

def execute(event_list,Venue):
	graph_dict={}
	

	for event in event_list:
		print "g"+str(event.first_day_preference)
		print "d"+str(event.first_time_preference)
		first = str(event.first_day_preference)+str(event.first_time_preference)
		second = str(event.second_day_preference)+str(event.second_time_preference)
		third = str(event.third_day_preference)+str(event.third_time_preference)
		if event.Venue == Venue:
			graph_dict[event.name]={first,second,third}
	
	print graph_dict
	timing= HopcroftKarp(graph_dict).maximum_matching()
	print timing

	for event in event_list:
		if (event.name).encode('ascii', 'ignore') in timing:
			event.Actual_time=timing[(event.name).encode('ascii', 'ignore')]
			event.Actual_day=event.Actual_time[0]
			event.Actual_time=event.Actual_time[1]
		
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"


def bpm(event_list):
	execute(event_list,'1')
	execute(event_list,'2')
	execute(event_list,'3')
	execute(event_list,'4')
	execute(event_list,'5')

	for event in event_list:
		x = Event.objects.get(name = event.name)
		x.Actual_time=event.Actual_time
		x.Actual_day=event.Actual_day
		x.save()
		x = Event.objects.get(name = event.name)	
		print x.Actual_time
	
	
	
	
	


	
