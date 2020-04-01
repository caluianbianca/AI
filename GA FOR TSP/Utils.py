from cmath import sqrt
from random import randint

def generateARandomPermutation(n):
        perm = [i for i in range(n)]
        pos1 = randint(0, n - 1)
        pos2 = randint(0, n - 1)
        perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
        return perm

def distance(matrix,x1,x2):
        #return matrix[x1][x2]
        return matrix.item((x1,x2))

def computeFitness(repres, problParams):
        totalDist = 0
        g = 0
        for gene in range(0, len(repres) - 1):
            #localDist = problParams["matrix"][repres[gene]][repres[gene+1]]
            localDist = problParams["matrix"].item((repres[gene], repres[gene+1]))
            totalDist += localDist
            g += 1
        #totalDist += problParams["matrix"][repres[g]][repres[0]]
        totalDist += problParams["matrix"].item((repres[g], repres[0]))
        return 1/float(totalDist)

def dist(repres, problParams):
    totalDist = 0
    g = 0
    for gene in range(0, len(repres) - 1):
        #localDist = problParams["matrix"][repres[gene]][repres[gene + 1]]
        localDist = problParams["matrix"].item((repres[gene], repres[gene+1]))
        totalDist += localDist
        g += 1
    #totalDist += problParams["matrix"][repres[g]][repres[0]]
    totalDist += problParams["matrix"].item((repres[g], repres[0]))
    return totalDist

