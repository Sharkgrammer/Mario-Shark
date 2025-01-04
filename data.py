import pandas as pd


class SharkData:

    def __init__(self):
        self.time_max = 0

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

        print(f"Time count max:{self.time_max}")

    def sort_data(self, shark=1):
        # Dataset contains 10 sharks, labeled 1-10
        if shark < 1 or shark > 10:
            return False

        group_by = self.df[self.df.Shark == f"WS{shark}"].groupby(['Shark', 'DT'])
        time_count = group_by["DT"].count().values

        data = group_by.mean(numeric_only=True)

        data = data.sort_index(level='Shark').reset_index()

        data = data.round({'Depth': 0, 'Longitude': 4})

        data['up'] = data.Depth.le(data.Depth.shift())
        data['right'] = data.Longitude.ge(data.Longitude.shift())
        data['time_count'] = time_count

        self.time_max = time_count.max()

        return data
