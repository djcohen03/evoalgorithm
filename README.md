# Evolutionary Algorithmic Engine
A Simple Multiprocessing Evolutionary Algorithmic Engine 


### Sample:

```
import evolution

def fitness(args):
    # A simple fitness function
    return args[1]

# Initialize EvoAlgorithm Engine with a 3-tuple of all 1's:
initial = (1, 1, 1)
evo = evolution.EvoAlgorithm(fitness, initial, variance=0.1)

# Increment 20 generations:
evo.run(20)

# Print a summary of the progress:
evo.log()

```
