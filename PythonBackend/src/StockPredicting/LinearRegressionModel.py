from sklearn.linear_model import LinearRegression


class LinearRegressionModel:

    @staticmethod
    def apply_linear_regression(X_train, y_train):
        clfreg = LinearRegression(n_jobs=-1)
        clfreg.fit(X_train, y_train)
        return clfreg