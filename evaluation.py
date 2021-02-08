from City import City
# compute fitness of an invidual for the 8-queen puzzle
def fitness_8queen (individual): # maximization
    
    M = 28
    check = 0
    fitness = 0
    

    distance = 1
    for i in range (0,len(individual)):
        origin = individual[i]
        if((i+1)<len(individual)):
            destination = individual[i+1]
        else:
            destination = individual[0]
        distance = distance + origin.getDistance(destination)
    fitness = 1/distance

    
    return fitness


