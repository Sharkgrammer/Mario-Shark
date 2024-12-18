import pandas as pd


class SharkData:

    def __init__(self):
        self.df = pd.read_csv('data.csv', sep=';')

        # Clean data
        self.df['DT'] = pd.to_datetime(self.df['DT'], format='%d/%m/%y %H:%M')
        self.df = self.df.drop(columns=['Latitude', 'ShoreDistance', 'Ships number', 'Length'])

    def describe_data(self, data=None):
        if data is None:
            data = self.df

        print("--- HEAD ---")
        print(data.head())
        print()

        print("--- SHAPE ---")
        print(data.shape)
        print()

        print("--- DESCRIBE ---")
        print(data.describe())
        print()

    def sort_data(self, shark=1):
        # Dataset contains 10 sharks, labeled 1-10
        if shark < 1 or shark > 10:
            return False

        data = self.df[self.df.Shark == f"WS{shark}"].groupby(['Shark', 'DT']).mean(numeric_only=True)

        data = data.sort_index(level='Shark').reset_index()

        data = data.round({'Depth': 0, 'Longitude': 4})

        data['up'] = data.Depth.le(data.Depth.shift())
        data['right'] = data.Longitude.ge(data.Longitude.shift())

        return data
