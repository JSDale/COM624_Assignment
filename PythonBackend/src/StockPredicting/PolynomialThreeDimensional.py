from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


class PolynomialThreeDimensional:
    @staticmethod
    def apply_quadratic_regression_three_dimensional(X_train, y_train):
        clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
        clfpoly3.fit(X_train, y_train)
        return clfpoly3