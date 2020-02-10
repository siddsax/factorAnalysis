# Import the plotting library
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import os
# Import the yfinance. If you get module not found error the run !pip install yfiannce from your Jupyter notebook
import yfinance as yf  
 
fl = open('names.pickle', 'rb')
names = pickle.load(fl)

os.makedirs('Data', exist_ok=True)

for i, nm in enumerate(names):
    if i > 2900:
        if i % 100 == 0:
            print("=============================================    {}/{}      =============================================".format(i, len(names)))
        data = yf.download(nm,'2010-01-01','2020-01-25')
        data.to_pickle("Data/{}.pkl".format(nm))


# skipped 2100 - 2200, 2800-2900