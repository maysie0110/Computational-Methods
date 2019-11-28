# May Trinh
# CMPS 4553 - Computational Methods

import numpy

pop_size = 10 #population size
chromosomes_length = 20 #chromosomes length
Pc = 0.7 # crossover rate
Pm = 0.001 #mutation rate
num_generation = 20

#create initial population with randomize 
def create_population(pop_size, chromosome_length):
    #set the initial population with an array of all zeros
    population = numpy.zeros((pop_size,chromosome_length), dtype=int)
    
    #loop through each row, assign a random number of ones 
    for i in range(pop_size):
        # get a random number from 0 - 20 
        num_ones = numpy.random.randint(0, chromosome_length)
        #change the zeros to ones
        population[i, 0:num_ones] = 1
        #shuffle the contents of each row
        numpy.random.shuffle(population[i])
    return population



# Calculating the fitness value of each solution in the current population.
# determines how fit an individual is and return a fitness score to each individual
# fitness scores = number of ones in each individual
def fitness_calculation (pop_size,population):
    fitness_scores = numpy.zeros((pop_size),dtype = int)
    for i in range(numpy.size(population,0)):
        fitness_scores[i] = numpy.count_nonzero(population[i, :] == 1)
    return fitness_scores
# with open("ga.txt","w") as outf:

#create initial population with 0s and 1s
population = create_population(pop_size,chromosomes_length)
print(population)
# print(type(population))
# print(numpy.size(population,0))
# print(numpy.count_nonzero(population[1, :] == 1))
fitness_scores = fitness_calculation(pop_size,population)
print(fitness_scores)
#fitness function 

