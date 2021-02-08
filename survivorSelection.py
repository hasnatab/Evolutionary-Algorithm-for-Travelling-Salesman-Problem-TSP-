
import random

# (mu+lambda) selection
def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):   
    population = []
    fitness = []


    total_pop = current_pop + offspring
    total_fitness = current_fitness + offspring_fitness
    current = 0
    maxim = 0
    maxIndex = 0
    chosenIndex = []
    # we then add to our populat the best fitnesses descending down, until we fill up the fitness and population
    for j in range(0,len(current_fitness)):
        current=0
        maxIndex=0
        maxim = 0
        for i in range(0,len(total_fitness)):
            current = total_fitness[i]
            if((current > maxim) and (i not in chosenIndex)):
                maxim = current
                maxIndex = i
        chosenIndex.append(maxIndex)
        fitness.append(maxim)
        population.append(total_pop[maxIndex])
        
        
 
    
    return population, fitness


# use offspring to replace the same number of the worst individuals in the current population
def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    
    population = []
    fitness = []
    

    
    population = current_pop.copy()
    fitness = current_fitness.copy()
    current_fit_x = 0
    current=0
    minim = 0
    minIndex = 0
    currentOff = 0
    # we will replace the smallest fitness value with a higher offsrping fitness if it exists
    for j in range(0,len(offspring_fitness)):
        currentOff = offspring_fitness[j]
        current = 0
        minim = fitness[0]
        minIndex = 0
        for i in range(0,len(fitness)):
            current = fitness[i]
            if(current<minim):
                minim = current
                minIndex = i
        if(currentOff >= minim):
            fitness[minIndex] = currentOff
            population[minIndex] = offspring[j]



    
    return population, fitness


# randomly uniformly pick individuals from the current population and new offspring
def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    
    population = []
    fitness = []


    total_pop = current_pop + offspring
    total_fitness = current_fitness + offspring_fitness
    index = 0
    while (len(fitness)< len(current_fitness)):
        index = random.randint(0,(len(total_fitness)-1))
        fitness.append(total_fitness[index])
        population.append(total_pop[index])
  
    
    return population, fitness
    


