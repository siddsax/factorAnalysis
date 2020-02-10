import pandas as pd
import pickle

exc = pd.read_excel('Yahoo Ticker Symbols - September 2017.xlsx')

names = []
for i in range(len(exc)):
    if i % 100 == 0:
        print("{}/{}".format(i, len(exc)))

    if exc['Unnamed: 4'][i] == 'Canada':
         names.append(exc['Yahoo Stock Tickers'][i])

print(names)
        
with open("names.pickle", "wb") as fp:
    pickle.dump(names, fp)


