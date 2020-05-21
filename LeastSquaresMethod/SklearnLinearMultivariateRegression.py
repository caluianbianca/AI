from sklearn import linear_model
from sklearn.metrics import mean_squared_error


class SklearnLinearMultivariateRegression:

    def __init__(self):
        self.__intercept = 0.0
        self.__coefs = []
        self.__regressor = linear_model.LinearRegression()

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs

    def fit(self, inputs, outputs):
        self.__regressor.fit(inputs, outputs)
        self.__intercept, self.__coefs = self.__regressor.intercept_, self.__regressor.coef_

    def predict(self, inputs):
        return self.__regressor.predict(inputs)

    def predictionError(self, predictedOutputs, realOutputs):
        return mean_squared_error(realOutputs, predictedOutputs)