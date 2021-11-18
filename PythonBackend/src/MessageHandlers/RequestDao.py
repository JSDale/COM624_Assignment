import json


class RequestDao:

    Ticker = None
    Source = None

    def __init__(self, Ticker, Source):
        self.Ticker = Ticker
        self.Source = Source
