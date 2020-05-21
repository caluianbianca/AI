import random

from numpy import average
from numpy.linalg import linalg

from MyMath import distance, avg, averageCentroid


class KMeans:

    def __init__(self, k=2, tol=0.001, max_iter=300):
        '''
        constructor
        :param k: no of clusters
        :param tol: tolerance - the clsuters are optimized if the centroid is not moving more than the tolerance
        :param max_iter: limit number of cycles
        '''
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.centroids = {}


    def fit(self, data):
        '''
        fit data
        :param data: train data we want to cluster
        :return: -
        '''
        #decide which inputs are the k centroids
        self.centroids = {}

        random.shuffle(data)
        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            pos = -1
            for centroid in self.centroids:
                pos += 1
                self.classifications[pos] = []

            for set in data:
                distances = [distance(set, self.centroids[centroid]) for centroid in self.centroids]
                # classification = min distance from set to centroids
                classification = distances.index(min(distances))
                # for each pos - centroid - we have all the corresponding sets
                self.classifications[classification].append(set)

            prev_centroids = dict(self.centroids)

            # move centroids
            for classification in self.classifications:
                self.centroids[classification] = averageCentroid(self.classifications[classification])

            # check if optimized
            optimized = True
            for pos in self.centroids:
                original_centroid = prev_centroids[pos]
                current_centroid = self.centroids[pos]
                if distance(original_centroid, current_centroid) > self.tol:
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        distances = [distance(data, self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification




