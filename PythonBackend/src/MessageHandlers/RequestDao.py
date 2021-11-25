
class RequestDao:

    Ticker = None
    Source = None
    ModelType = None

    def __init__(self, Ticker, Source, ModelType):
        self.Ticker = Ticker
        self.Source = Source
        self.ModelType = ModelType
