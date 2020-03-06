#Howard Kim
#for comp131 Spring 2019

#a box is represented by a tuple (weight, importance, included)
#each list of boxes is a genome
#a population is a list of tuples of (genome, corresponding fitness value)

import random

def getfitness(genome, maxweight): #returns the fitness value of a genome
  fitness = 0
  weight = 0
  for box in genome:
    fitness = fitness + box[1] * box[2]
    weight = weight + box[0] * box[2]
  if weight > maxweight:
    fitness = fitness - (weight - maxweight)
  return fitness
    

def default(popsize, maxweight): #returns a population of boxlists ordered by fitness, most fit first, for the default knapsack problem
  population = []
  for i in range(popsize):
    genome = []
    genome.append((20, 6, random.getrandbits(1)))
    genome.append((30, 5, random.getrandbits(1)))
    genome.append((60, 8, random.getrandbits(1)))
    genome.append((90, 7, random.getrandbits(1)))
    genome.append((50, 6, random.getrandbits(1)))
    genome.append((70, 9, random.getrandbits(1)))
    genome.append((30, 4, random.getrandbits(1)))
    population.append((genome))
  population.sort(reverse=True, key=lambda x: getfitness(x, maxweight))
  return population

def cull(population): #stochastically reduces the population by half, with less fit boxlists being more likely to be removed
  newpopulation = []
  popsize = len(population)
  newpopsize = popsize/2
  survivalchance = popsize
  while len(newpopulation) < newpopsize:
    for genome in population:
      if random.randrange(popsize) < survivalchance:
        newpopulation.append(genome)  
        survivalchance = survivalchance - 1
  return newpopulation

def doublepop(population, maxweight): #randomly selects pairs of genomes within a population to generate children, using crossover and mutation
  newpop = []
  while population:
    parent1 = population.pop()
    newpop.append(parent1)
    if population:
      parent2 = population.pop(random.randrange(len(population)))
      newpop.append(parent2)
      children = crossover(parent1, parent2)
      child1 = mutate(children[0])
      child2 = mutate(children[1])
      newpop.append(child1)
      newpop.append(child2)
  newpop.sort(reverse=True, key=lambda x: getfitness(x, maxweight))
  return newpop
    

def crossover(genome1, genome2): #crosses over two genomes to make two children
  cutpoint = random.randrange(len(genome1))
  child1 = genome1[:cutpoint] + genome2[cutpoint:]
  child2 = genome1[:cutpoint] + genome2[cutpoint:]
  return [child1, child2]


def mutate(genome): #randomly mutates boxes in a newly generated boxlist with a 1/100 chance
  for box in genome:
    if random.randrange(100) == 1:
      if box[2] == 0:
        box[2] == 1
      else:
        box[2] == 0
  return genome


def geneticsearch(default, maxweight, generations):
  while generations > 0:
    population = cull(default)
    population = doublepop(population, maxweight)
    generations = generations - 1
  mostfit = population[0]
  return mostfit
  

#The following requires python3 to function properly. If using python2, comment out everything not in the following "elif" section.

yn = str(input(("Welcome to the knapsack problem. Would you like to solve with custom parameters? (y/n) ")))
if yn == "y":
  popsize = int(input("Enter the number of the initial population\n"))
  generations = int(input("Enter the number of generations\n"))
  maxweight = int(input("Enter the maximum weight carried\n"))
  mostfit = geneticsearch(default(popsize, maxweight), maxweight, generations) #for testing
  print("The highest total importance found is " + str(getfitness(mostfit, maxweight)) + " with the following boxes included: ")
  for box in mostfit:
    if box[2] != 0:
      print("weight: " + str(box[0]) + " importance: " + str(box[1]))
elif yn == "n":
  mostfit = geneticsearch(default(1000, 120), 120, 100) #for testing
  print("Using default parameters: Boxes provided by assignment, maximum weight of 120, population size of 1000, generation number of 100, mutation percentage of 1%.")
  print("The highest total importance found is " + str(getfitness(mostfit, 120)) + " with the following boxes included: ")
  for box in mostfit:
    if box[2] != 0:
      print("weight: " + str(box[0]) + " importance: " + str(box[1]))
  
