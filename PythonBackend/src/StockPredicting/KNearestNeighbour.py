from sklearn.neighbors import KNeighborsRegressor


class KNearestNeighbour:
    @staticmethod
    def apply_k_nearest_neighbour(X_train, y_train):
        clfknn = KNeighborsRegressor(n_neighbors=2)
        clfknn.fit(X_train, y_train)
        return clfknn