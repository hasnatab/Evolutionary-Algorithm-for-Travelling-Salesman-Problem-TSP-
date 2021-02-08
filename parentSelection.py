import random

#multi-pointer selection (MPS)
def MPS(fitness, mating_pool_size):
     
    selected_to_mate = [] # list of the indices of picked parents

    #let's set up the probablity distribution
    a= []
    x = 0
    minim = fitness[0]
    current = 0
    total = 0

    for i in range(0,len(fitness)):
        current = fitness[i]
        if(current<minim):
            minim = current
            
    for i in range(0,len(fitness)):
        current = fitness[i]
        total = total + current
    for i in  range(0,len(fitness)):
        x = (fitness[i])/total
        a.append(x)
    #each probability in a[] corresponds to the same index for the parents a[0]is the probability  for parent in index 0
    # MPS implementation
    current_member = 0
    i=0
    while(current_member < mating_pool_size):
        r= random.uniform(0,(1/mating_pool_size))
        while(r <= a[i] and (len(selected_to_mate)<mating_pool_size)):
            selected_to_mate.append(i)
            r = r + (1/mating_pool_size)
            current_member= current_member +1
        i=i+1
        if(i>(len(a)-1)):
            i=0
       # print(selected_to_mate)
    

    return selected_to_mate


#tournament selection without replacement
def tournament(fitness, mating_pool_size, tournament_size):
    
    selected_to_mate = [] # list of the indices of picked parents


    current_member = 0
    while(current_member< mating_pool_size):
        #pick k individuals and compare them and denote best as i
        count = 0 # count is k
        i=0
        chosen = [] # store our k individuals
        while(count < tournament_size):
            index1 = random.randint(0,(len(fitness)-1))
            if(index1 not in chosen):
                chosen.append(index1)
                count = count +1
                for j in range(0,len(chosen)):
                    current = chosen[j]
                    if(fitness[current]>=fitness[i]):
                        i=current;
        selected_to_mate.append(i)
        current_member = current_member + 1
            
    
    return selected_to_mate


#randomly uniformly pick parents
def random_uniform (population_size, mating_pool_size):

    selected_to_mate = [] # list of the indices of picked parents


    i=0
    index = 0
    while(i<mating_pool_size):
        index=random.randint(0,(population_size-1))
        selected_to_mate.append(index)
        i = i+1

    
    return selected_to_mate

