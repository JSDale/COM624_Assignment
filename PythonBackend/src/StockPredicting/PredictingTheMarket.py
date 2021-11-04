import pandas_datareader.data as web
import datetime
import math
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


class PredictingTheMarket:

    __information_source = 'yahoo'
    __start_date = datetime.datetime(2010, 1, 1)
    __end_date = datetime.datetime.now()
    __stock_type = ['Adj Close']

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
        dfreg = dataframe.loc[:, ['Adj Close']]
        dfreg['HL_PCT'] = (dataframe['High'] - dataframe['Low']) / dataframe['Close'] * 100.0
        dfreg['PCT_change'] = (dataframe['Close'] - dataframe['Open']) / dataframe['Open'] * 100.0
        print(dfreg)
        return dfreg

    def predict(self, dfreg):
        # drop missing values
        dfreg.fillna(value=-99999, inplace=True)
        print(dfreg.shape)
        # separate to 1% of the data to forecast
        forecast_out = int(math.ceil(0.01 * len(dfreg)))

        # Separating label here, to predict the Adjusted close.
        forecast_col = 'Adj Close'
        dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
        x = np.array(dfreg.drop(['label'], 1))

        x = preprocessing.scale(x)

        x_lately = x[-forecast_out:]
        x = x[:-forecast_out]

        y = np.array(dfreg['label'])
        y = y[:-forecast_out]

        print(f'dimension of x: {x.shape}')
        print(f'dimension of y: {y.shape}')

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Linear regression
        clfreg = LinearRegression(n_jobs=-1)
        clfreg.fit(x_train, y_train)

        clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
        clfpoly2.fit(x_train, y_train)

        clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
        clfpoly3.fit(x_train, y_train)

        clfknn = KNeighborsRegressor(n_neighbors=2)
        clfknn.fit(x_train, y_train)
        
        # Testing
        confidencereg = clfreg.score(x_test, y_test)
        confidencepoly2 = clfpoly2.score(x_test, y_test)
        confidencepoly3 = clfpoly3.score(x_test, y_test)
        confidenceknn = clfknn.score(x_test, y_test)

        print("The linear regression confidence is ", confidencereg)
        print("The quadratic regression 2 confidence is ", confidencepoly2)
        print("The quadratic regression 3 confidence is ", confidencepoly3)
        print("The knn regression confidence is ", confidenceknn)

