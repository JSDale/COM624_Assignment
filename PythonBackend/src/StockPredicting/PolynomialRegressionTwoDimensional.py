from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


class PolynomialRegressionTwoDimensional:
    @staticmethod
    def apply_quadratic_regression_two_dimensions(X_train, y_train):
        clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
        clfpoly2.fit(X_train, y_train)
        return clfpoly2