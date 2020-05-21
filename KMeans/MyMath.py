from cmath import sqrt


def distance(a, b):
    '''
    Euclidian Distance between a and b
    :param a: list
    :param b: list
    :return: int
    '''
    summ = 0
    for i in range(len(a)):
        summ += (a[i] - b[i]) ** 2
    return sqrt(summ).real

def avg(l):
    '''
    Average value of values in list
    :param l: list
    :return: int
    '''
    total = 0
    for el in l:
        total += el
    return total / len(l)

def averageCentroid(centroids):
    feats = [0 for _ in range(len(centroids[0]))]
    for centroid in centroids:
        for i in range(len(centroid)):
            feats[i] += centroid[i]

    for i in range(len(feats)):
        feats[i] = feats[i] / len(centroids)

    return feats