from random import randint, random, Random

import numpy

from Chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param  # popSize, noGen
        self.__problParam = problParam
        self.__population = []

    @property
    def param(self):
        return self.__param

    @property
    def problParam(self):
        return self.__problParam

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for i in range(1, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 2)
        pos2 = randint(0, self.__param['popSize'] - 2)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def rouletteSelection(self):
        maxx = sum(Chromosome.fitness for Chromosome in self.__population)
        rand = numpy.random.uniform(0, maxx)
        summ = 0
        for pos in range(0, len(self.__population)):
            summ += self.__population[pos].fitness
            if summ > rand:
                return pos;

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize']):
            #p1 = self.__population[self.selection()]
            p1 = self.__population[self.rouletteSelection()]
            #p2 = self.__population[self.selection()]
            p2 = self.__population[self.rouletteSelection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            # p1 = self.__population[self.selection()]
            p1 = self.__population[self.rouletteSelection()]
            # p2 = self.__population[self.selection()]
            p2 = self.__population[self.rouletteSelection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres, self.__problParam)
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            # p1 = self.__population[self.selection()]
            p1 = self.__population[self.rouletteSelection()]
            # p2 = self.__population[self.selection()]
            p2 = self.__population[self.rouletteSelection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
