from instance_generator import *
from processor import *
from greedy import *
import genetic as ga

task_array = []

NUM_OF_PROC = 30  # Number of processors
NUM_OF_TASKS = 300  # Number of tasks
MIN_TASK_TIME = 100  # Min value of task length for generator
MAX_TASK_TIME = 1000  # Max value of task length for generator

#given_data = generate(task_array, NUM_OF_TASKS, MIN_TASK_TIME, MAX_TASK_TIME)  # Generating instance with random task lengths
#print(f'Number of processors: {NUM_OF_PROC}\nNumber of tasks: {NUM_OF_TASKS}\nCollected data: {given_data}')
#noprocs = NUM_OF_PROC
save_generated(task_array, NUM_OF_PROC, NUM_OF_TASKS, "30x300")  # Saving generated array to file
m25_data, m25_noprocs, m25_notasks = read_data("m25")  # Reading data from given file
m50_data, m50_noprocs, m50_notasks = read_data("m50")  # Reading data from given file
m10n200_data, m10n200_noprocs, m10n200_notasks = read_data("m10n200")  # Reading data from given file
m50n200_data, m50n200_noprocs, m50n200_notasks = read_data("m50n200")  # Reading data from given file
m50n1000_data, m50n1000_noprocs, m50n1000_notasks = read_data("m50n1000")  # Reading data from given file
m40n1000_data, m40n1000_noprocs, m40n1000_notasks = read_data("m40n1000")  # Reading data from given file
m30n300_data, m30n300_noprocs, m30n300_notasks = read_data("m30n300")  # Reading data from given file
d1_data, d1_noprocs, d1_notasks = read_data("d1")  # Reading data from given file


#GENETIC ALGORITHM VARIABLES
POPULATION_SIZE = 20
MUTATION_PROBABILITY = 0.20
NUM_GENERATIONS = 300000


noprocs = m25_noprocs
data = m25_data
optimum = sum(data)/noprocs

#PREZENTACJA WYNIKÓW
print(f'Wartoś optymalna to: {optimum}')
print(f'Wartoś otrzymana przy użyciu algorytmu zachłannego: {max_proc_time(noprocs, data)}')

ga.run(data,noprocs, POPULATION_SIZE, NUM_GENERATIONS, MUTATION_PROBABILITY)




