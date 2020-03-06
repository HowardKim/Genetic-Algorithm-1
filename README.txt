Genetic Algorithm for the Knapsack Problem
Howard Kim

Each box is represented by a tuple with the parameters [weight, importance, included]. Included is 1 if yes, 0 if no. This list of boxes is the genome. Every list of boxes is a potential solution, and a large number of possible solutions (default 1000) will be evaluated by a fitness function. Those with the highest fitness functions will be more likely to survive to the next generation. These survivors will sexually reproduce with other survivors to produce the next generation. Upon creation, the new units will have a small mutation chance. This process will be repeated for K generations (default K=100) when the most fit specimen will be selected as a solution.
The fitness function is determined by the total importance of the included boxes (importance is the sum of box[0] * box[2] for all boxes in genome, weight is the sum of box[1] * box[2] for all boxes in genome). If overweight, a value of (weight - maximum weight) is subtracted from the fitness function. The population is then sorted by the fitness of each genome.

Culling: For a population of size X, the 1st most fit specimen will have an X/X chance of reproducing, the second will have chance (X-1)/X chance of reproducing, etc. until X/2 specimens are selected, repeating the process if necessary if X/2 specimens are not selected in the first run through.

Reproducing: Of the survivors, random pairs will be selected to crossover with each other to produce new specimens. The population will generate new specimens via the crossover and mutation functions. A random cutoff point will be determined to cross over two separate genomes and generate two novel children. These children will then undergo a chance of mutation, with each of the box values' "included" value having a 1% chance of being flipped. The fitness level of these children will then be evaluated and added to the population. The process will now repeat until K generations have been reached.

This program must be run using python3 to function properly.

A total of 5 hours was spent on this assignment. No assistance from a person was received.
