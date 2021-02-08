
import random
from random import shuffle
# initialize a population of permutation
def permutation (pop_size, cityL):
    
    population = []
    

    for i in range (0,pop_size):
        shuffle(cityL)
        population.append(cityL)

    
    return population   
	

