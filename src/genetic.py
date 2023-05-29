from random import random, randint

def createRandom(data, noprocs):
    random_individual = [[] for p in range(noprocs)]
    for task in data:
        choosen_proc = randint(0,noprocs - 1)
        random_individual[choosen_proc].append(task)
    return random_individual
#creates genotype for given individual
#[0,1,2,1,1,0,0,3, ...]
#Where 0, 1, 2... stands for proc number
def createGenotype(data,individual):
    genotype = []
    for task in data:
        for proc_index, proc in enumerate(individual):
            if task in proc:
                genotype.append(proc_index)
                task_index = proc.index(task)
                proc[task_index] = -1
                break
    return genotype
#Transforms genotype to list of tasks for each proc
#[P1[task1,task2], P2[task3,task4], ...]
def readGenotype(data, noprocs, genotype):
    procs = [[] for p in range(noprocs)]
    for task_index, proc_index in enumerate(genotype):
        procs[proc_index].append(data[task_index])
    return procs

#Checks fittness according to smallest max_proc_time of individuals
def fittness(data, noprocs, genotype):
    curr_max_time = 0
    individual = readGenotype(data,noprocs,genotype)
    for proc in individual:
        max_proc_time = sum(proc)
        if curr_max_time < max_proc_time:
            curr_max_time = max_proc_time
    return -1 * curr_max_time

#Selection sorts by fittness and takes two fittest individuals
def selection(data, noprocs, population):
    fittness_sorted = sorted(population, key=lambda genotype: fittness(data, noprocs, genotype), reverse=True)
    genA = fittness_sorted[0]
    genB = fittness_sorted[1]
    return (genA, genB)

#Crossover created two children from best genotypes, takes half of genA and half of genB and combines them child1 [1st_half_genA+2nd_half_genB]
#child2 [2nd_half_genA + 1st_half_genB]
def crossover(genA, genB):
    gen_len = len(genA)
    half_gen_len = round(gen_len)
    child1 = genA[:half_gen_len] + genB[half_gen_len:]
    child2 = genA[half_gen_len:] + genB[:half_gen_len]
    return (child1, child2)

#Mutation swaps created chilrden from crossover procedure and swaps with two least fit children
def mutation(noprocs, population, MUTATION_PROBABILITY):
    for gen in population:
        if random() < MUTATION_PROBABILITY:
            index = randint(0, len(gen) - 1)
            new_proc_index = randint(0, noprocs - 1)
            gen[index] = new_proc_index

def initial_population(data, noprocs, POPULATION_SIZE):
    initial_population = []
    for i in range(POPULATION_SIZE):
        individual = createRandom(data, noprocs)
        genotype = createGenotype(data, individual)
        initial_population.append(genotype)
    return initial_population

def random_generator(data, noprocs):
    return lambda: createRandom(data, noprocs)

def geneticAlg(initial_population, data, noprocs, NUM_GENERATIONS, MUTATION_PROBABILITY):
    population = initial_population
    #fittness "start" value
    best_fittness = 100000
    best_genotype = None
    curr_num_generations = 0
   
    while curr_num_generations < NUM_GENERATIONS:

        # SELECTION
        fittest_individuals = selection(data, noprocs, population)

        # CROSSOVER
        child1, child2 = crossover(fittest_individuals[0], fittest_individuals[1])

        least_fit = min(population, key=lambda genotype: fittness(data, noprocs, genotype))
        least_fit_index = population.index(least_fit)
        population[least_fit_index] = child1

        second_least_fit = min(population, key=lambda genotype: fittness(data, noprocs, genotype))
        second_least_fit_index = population.index(second_least_fit)
        population[second_least_fit_index] = child2

        # MUTATION
        mutation(noprocs, population, MUTATION_PROBABILITY)

        current_best = abs(fittness(data, noprocs, fittest_individuals[0]))
        if current_best < best_fittness:
            best_fittness = current_best
            best_genotype = fittest_individuals[0]
            no_progress_counter = 0
        curr_num_generations += 1
    #else: #Comment to see the results at every step
        #print(fittest_individuals[0])
        print(f'Wartość otrzymana przy użyciu algorytmu genetycznego: {best_fittness}')


def run(data, noprocs, POPULATION_SIZE, NUM_GENERATIONS, MUTATION_PROBABILITY):
    #Generating random poulations of POPULATION_SIZE from given data
    init_population = initial_population(data, noprocs, POPULATION_SIZE)
    #Genetic Algorithm initialization
    geneticAlg(init_population, data, noprocs, NUM_GENERATIONS, MUTATION_PROBABILITY)