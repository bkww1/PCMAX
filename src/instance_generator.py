import random
import sys
sys.path.append('../')

def generate(task_array,num_of_tasks,min_t_num,max_t_num):
	
	for i in range(num_of_tasks):
		task_array.append(random.randint(min_t_num,max_t_num))
	return task_array
	
	
def save_generated(list_name,num_of_proc,num_of_tasks,file_name):
	with open(f'../data/{file_name}.txt', 'w') as file:
		file.write(str(num_of_proc) + '\n')
		file.write(str(num_of_tasks) + '\n')
		file.write('\n'.join(map(str, list_name)))


def read_data(filename):
	data_array = []
	with open(f'../data/{filename}.txt', 'r') as file:
		num_of_proc = int(file.readline())
		num_of_tasks = int(file.readline())
		
		for row in file:
			data_array.append(int(row))
	
	return data_array, num_of_proc, num_of_tasks