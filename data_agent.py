import pandas as pd

class DataAgent:
    def __init__(self, path):
        self.path = path

    def load(self):
        df = pd.read_excel(self.path)
        x = df.iloc[:,0].values
        y = df.iloc[:,1].values
        return x, y
