import json


class StockMessageDao:

    GraphLocation = None
    Predictions = []

    def __init__(self, graph_filepath, predictions):
        self.Predictions = predictions
        self.GraphLocation = graph_filepath

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
