from instance_generator import *
from processor import *

#Greedy algorithm searches processor with lowest proc time and appends it with next task 
class GreedyAlg():
	def run(self,noprocs,given_data):
		self.processors_list = []

		for x in range(noprocs):
			self.processors_list.append(Processor(x))

		for y in given_data:
			self.find_lowest_time(self.processors_list).append_tasks(y)

		return self.processors_list
	
	def find_lowest_time(self,processors_list):
		return min(processors_list, key = lambda processor: processor.time)

	def proctimes(self,processors_list):
		proctimes =[]
		for x in processors_list:
			proctimes.append(x.time)
		return proctimes
	
	def printprocs(self,processors_list):
		proc_list = []
		for x in processors_list:
			proc_list.append(x.time)
		return proc_list

def max_proc_time(noprocs,given_data):
	proc_list = GreedyAlg().run(noprocs,given_data)
	proc_list_translated = GreedyAlg().printprocs(proc_list)
	return max(proc_list_translated)