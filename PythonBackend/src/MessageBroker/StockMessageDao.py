import json


class StockMessageDao:

    GraphLocation = None
    ModelConfidence = None

    def __init__(self, graph_filepath, confidence):
        self.ModelConfidence = confidence
        self.GraphLocation = graph_filepath

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
