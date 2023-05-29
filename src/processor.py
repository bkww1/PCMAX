from instance_generator import *

class Processor():
	def __init__(self,num):
		self.num = num
		self.time = 0
		self.task_list = [] 

	def append_tasks(self,task):
		self.task_list.append(task)
		self.time += task

	