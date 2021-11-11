import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model

from FileManipulation import SavingToFiles


class PredictingTheMarket:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2019, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']
    __save_to_files = SavingToFiles.SaveToFiles()

    def get_stock_dataframe(self, ticker):
        try:
            print('getting data...')
            dataframe = web.DataReader(ticker, self.__information_source, start=self.__start_date,
                                       end=self.__end_date)
            return dataframe
        except Exception as e:
            print(f'error: {str(e)}')

    def get_dfreg(self, dataframe):
        print(dataframe)
        dfreg = dataframe.loc[:, ['Adj Close', 'Volume']]
        print(dfreg)
        return dfreg

    def predict(self, dfreg):
        # drop missing values
        dfreg[:].fillna(0, inplace=True)
        self.__save_to_files.save_to_json(dfreg, "drfeg.json")
        print(dfreg.shape)
        dfreg['label'] = dfreg['Adj Close']

        X = np.array(dfreg.drop(['label'], 1))
        print(X)

        Y = dfreg.keys()

        # Split the data into training/testing sets
        X_train = X[:-20]
        X_test = X[-20:]

        # Split the targets into training/testing sets
        Y_train = Y[:-20]
        Y_test = Y[-20:]

        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(X_train, Y_train)

        # Make predictions using the testing set
        Y_pred = regr.predict(X_test)

        # The coefficients
        print("Coefficients: \n", regr.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(Y_test, Y_pred))
        # The coefficient of determination: 1 is perfect prediction
        print("Coefficient of determination: %.2f" % r2_score(Y_test, Y_pred))

        # Plot outputs
        plt.scatter(X_test[:, 0], Y_test, color="black")
        plt.plot(X_test, Y_pred, color="blue", linewidth=3)

        plt.xticks(())
        plt.yticks(())
        self.__save_to_files.save_graph_as_png('Linear_testing2.png')
