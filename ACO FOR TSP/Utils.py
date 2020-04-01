from pandocfilters import Math


def length(ant, graph):
    # compute length of ant's trail
    dist = 0
    for pos in range(0, len(ant.trail) - 1):
        localDistance = graph.item((ant.trail[pos], ant.trail[pos + 1]))
        dist += localDistance
    dist += graph.item(ant.trail[(len(ant.trail) - 1)], ant.trail[0])
    return dist


def distance(p1, p2, graph):
    return graph.item((p1, p2))


# desirability = 1 / distance
def probability(pheromoneAmount, desirability, pheromoneImportance, distancePriority, denominator):
    numerator = computeNumerator(pheromoneAmount, desirability, pheromoneImportance, distancePriority)
    # denominator =  pheromone += Math.pow(trails[i][l], alpha) * Math.pow(1.0 / graph[i][l], beta);
    return numerator / denominator


def computeNumerator(pheromoneAmount, desirability, pheromoneImportance, distancePriority):
    return (pheromoneAmount ** pheromoneImportance) * (desirability ** distancePriority)
