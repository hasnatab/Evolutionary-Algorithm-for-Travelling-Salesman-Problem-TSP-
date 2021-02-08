

from City import City

import random
import numpy
import math

import initialization
import evaluation
import recombination
import mutation
import parentSelection
import survivorSelection

def main():
   
    random.seed()
    numpy.random.seed()

    string_length = 8
    popsize = 20
    mating_pool_size = int(popsize*0.5) # has to be even
    tournament_size = 3
    mut_rate = 0.2
    xover_rate = 0.9
    gen_limit = 100

    # initialize population
    cityList = []
    c1=City(2,5,"c1")
    c2=City(4,5,"c2")
    c3=City(9,5,"c3")
    c4=City(12,10,"c4")
    c5=City(20,11,"c5")
    c6=City(13,14,"c6")
    c7=City(20,19,"c7")
    c8=City(21,12,"c8")
    c9=City(210,120,"c9")
    c10=City(165,22,"c10")
    c11=City(35,26,"c11")
    c12=City(50,50,"c12")
    c13=City(205,120,"c13")
    c14=City(154,20,"c14")
    c15=City(150,200,"c15")
    c16=City(130,150,"c16")
    c17=City(135,125,"c17")
    c18=City(110,145,"c18")
    c19=City(25,132,"c19")
    c20=City(60,124,"c20")
    cityList.append(c1)
    cityList.append(c2)
    cityList.append(c3)
    cityList.append(c4)
    cityList.append(c5)
    cityList.append(c6)
    cityList.append(c7)
    cityList.append(c8)
    cityList.append(c9)
    cityList.append(c10)
    cityList.append(c11)
    cityList.append(c12)
    cityList.append(c13)
    cityList.append(c14)
    cityList.append(c15)
    cityList.append(c16)
    cityList.append(c17)
    cityList.append(c18)
    cityList.append(c19)
    cityList.append(c20)
    gen = 0 # initialize the generation counter
    population = initialization.permutation(popsize, cityList)
    fitness = []
    for i in range (0, popsize):
        fitness.append(evaluation.fitness_8queen(population[i]))
    print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))

    # evolution begins
    while gen < gen_limit:
        
        # pick parents
        #parents_index = parentSelection.MPS(fitness, mating_pool_size)
        parents_index = parentSelection.tournament(fitness, mating_pool_size, tournament_size)
#        parents_index = parentSelection.random_uniform(popsize, mating_pool_size)

        # in order to randomly pair up parents
        random.shuffle(parents_index)
    
        # reproduction
        offspring =[]
        offspring_fitness = []
        i= 0 # initialize the counter for parents in the mating pool
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
        
            # recombination
            if random.random() < xover_rate:            
                off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2)
        
            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness_8queen(off1))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness_8queen(off2))
            i = i+2  # update the counter

        # form the population of next generation
        population, fitness = survivorSelection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
#        population, fitness = survivorSelection.replacement(population, fitness, offspring, offspring_fitness)
#        population, fitness = survivorSelection.random_uniform(population, fitness, offspring, offspring_fitness)
        
        gen = gen + 1  # update the generation counter
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
        
    # evolution ends
    
    # print the final best solution(s)
    k = 0
    for i in range (0, popsize):
        if fitness[i] == max(fitness):
            print("best solution", k)
            for j in range(0,len(population[i])):
                print("city : ",population[i][j].name ,"position : (", population[i][j].x , ",",population[i][j].y,")")
            print("fitness :", fitness[i])
            k = k+1

# end of main


main()





