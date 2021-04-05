import numpy as np
import multiprocessing

class EvoAlgorithm(object):
    def __init__(self, algorithm, inputs, variance=1.):
        ''' Evolutionary Algorithm to Apply Random Genetic Mutations To a
            Sample And Breed to Select the Best
        '''
        self.algorithm = algorithm
        self.current = np.array(inputs)
        self.inputs = [np.array(inputs)]
        self.outputs = [self.algorithm(self.current)]
        self.variance = variance
        self.generation = 1
        self.generations = {}

        # Save the current generation:
        self.savecurrent()

    @classmethod
    def breed(cls, inputs, variance, children):
        ''' Breen N new children based on the given inputs and the given variance
        '''
        # Get a set of random genetic mutations:
        count = len(inputs)
        variations = np.random.normal(1., variance, children * count)
        variations = variations.reshape((children, count))

        # Apply the genetic mutations to the inputs array to create a new
        # generation:
        offspring = [variations[index] * inputs for index in range(children)]
        return offspring

    def savecurrent(self):
        ''' Save the current generation inputs in the self.generations dictionary
        '''
        self.generations[self.generation] = {
            'best': self.current,
            'inputs': self.inputs,
            'outputs': self.outputs,
        }

    def log(self):
        ''' Print out a summary of all generations
        '''
        for index, generation in self.generations.iteritems():
            print '%sth Generation:' % index
            bestindex = np.argmax(generation['outputs'])
            for i, inputs in enumerate(generation['inputs']):
                print '    %s: %s %s' % (
                    inputs,
                    generation['outputs'][i],
                    '*' if i == bestindex else ''
                )

    def run(self, ngenerations, children=4):
        ''' Run the algorithm through N evolutionary generations
        '''
        for _ in range(ngenerations):
            self.generation += 1
            print 'Running Generation %s...' % self.generation

            # Get new generations inputs:
            self.inputs = self.breed(self.current, self.variance, children)

            # Apply the fitness algorithm to each of our new inputs:
            pool = multiprocessing.Pool(children)
            self.outputs = pool.map(self.algorithm, self.inputs)
            self.current = self.inputs[np.argmax(self.outputs)]
            pool.close()

            # Be sure to save a copy of the most recent generation
            self.savecurrent()

    def __repr__(self):
        '''
        '''
        return '%sth-Generation EvolutionaryAlgorithm: %s' % (self.generation, self.algorithm.__name__)



if __name__ == '__main__':

    def algo(args):
        return args[1]

    initial = (1, 2, 3)
    evo = EvoAlgorithm(algo, initial, variance=0.01)
    evo.run(100)
    evo.log()
