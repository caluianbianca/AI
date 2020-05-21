from matplotlib.pyplot import scatter


class UI:

    def __init__(self, kmeans, data):
        self.classifier = kmeans
        self.data = data

    def run(self):
        self.classifier.fit(self.data.trainInput)

        for centroid in self.classifier.centroids:
            print("centroid ", centroid, self.classifier.centroids[centroid])

        for set in self.data.testInput:
            classification = self.classifier.predict(set)
            print("data: ", str(set), " class: ", classification)

