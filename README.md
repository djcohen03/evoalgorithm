# Evolutionary Algorithmic Engine
A Simple Multiprocessing Evolutionary Algorithmic Engine


### Sample:

```
import evolution
def fitness(args):
    # A simple fitness function which prioritizes arg[1]
    return args[1]

# Initialize EvoAlgorithm Engine with a 3-tuple of all 1's:
initial = (1, 1, 1)
evo = evolution.EvoAlgorithm(fitness, initial, variance=0.1)

# Increment 20 generations:
evo.run(20)

# Print a summary of the progress:
evo.log()

1st Generation:
    [1 1 1]: 1 *
2nd Generation:
    [0.82057161 0.96278154 0.8996533 ]: 0.9627815379270728
    [0.99341601 0.8801949  1.12726066]: 0.8801949020704615
    [1.04823369 0.94818756 0.99368782]: 0.9481875616907303
    [0.93619732 1.0104569  0.92525416]: 1.0104568978249004 *
...
20th Generation:
    [0.78235136 4.91182121 1.06928125]: 4.911821211459355
    [0.7817377  5.20303069 0.91406788]: 5.203030688649108
    [0.72620195 5.67738095 1.06588912]: 5.677380948961333 *
    [0.67172924 4.96281459 1.18054785]: 4.962814591859316
```
