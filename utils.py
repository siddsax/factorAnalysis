import pandas as pd
import glob
import os
import numpy as np
from scipy.stats import linregress

def deleteNonExists(stock, path='Data'):

    df = pd.read_pickle(os.path.join(path, stock + '.pkl'))
    c1 = format(df.iloc[-1].name).split(' ')[0] != '2020-01-24'
    c2 = format(df.iloc[-1].name).split(' ')[0] != '2020-01-23'
    c3 = df['Volume'][-1] < 50000
    c4 = df['High'][-1] < .4
    if (c1 and c2) or (c3) or c4:
        os.remove(os.path.join(path, stock + '.pkl'))
        print(stock)
        return 0
    else:
        return 1

def getMomentum(closes, atr, riskFactor = 0.001):
    
    returns = np.log(closes)
    # import pdb;pdb.set_trace()
    x = np.arange(len(returns))
    slope, _, rvalue, _, _ = linregress(x, returns)
    value = ((1 + slope) ** 252) * (rvalue ** 2)
    score = value*riskFactor/atr
    return score

def getATR(df, window=14):

    sm = 0.0
    for i, row in df.iterrows():
        tf = max( np.abs(row['Low'] - row['Close']), np.abs(row['High'] - row['Close']), np.abs(row['High'] - row['Low']) )
        sm += tf
    
    return sm/len(df)

def getBestMomentum(stocks, numBest, wMean=30, wStock=5, path='Data'):
    atrs = []
    momentums = pd.DataFrame(columns=[stock for stock in stocks])
    for i, stock in enumerate(stocks):
        if i % 100 == 0:
            print(i)
        df = pd.read_pickle(os.path.join(path, stock + '.pkl'))
        if df['Volume'].iloc[-1] < 50000:
            continue

        atr10 = getATR(df, window=len(df))
        df = df.iloc[-(wMean + wStock):]

        try:
            momentums[stock] = df['Close'].rolling(wStock).apply(getMomentum, args={atr10}, raw=False)[wStock:]
        except:
            print(stock)
        atrs.append(atr10)


    momentums.loc['mean'] = momentums.median()
    momentums = momentums.iloc[-1]

    bests = momentums.sort_values(ascending=False).index[:numBest]
    return bests, momentums, atrs
