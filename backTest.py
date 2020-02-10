from backtesting.test import SMA
import pandas as pd
import backtrader as bt
import os
import glob
from strategy import TestStrategy
import datetime

# cerebro.broker.setcommission(commission=0.001)

cerebro = bt.Cerebro()
# cerebro.addstrategy(TestStrategy)

path = 'Data'
stocks = [pth.split('/')[-1][:-4] for pth in glob.glob(os.path.join(path,'*.pkl'))]

GSPTSE = pd.read_pickle(os.path.join(path, 'GSPTSE.pkl'))
cerebro.adddata(bt.feeds.PandasData(dataname=GSPTSE))


lst = [164, 228]
for i, stock in enumerate(stocks):
    if i in lst:
        import pdb;pdb.set_trace()
        continue
    df = pd.read_pickle(os.path.join(path, stock + '.pkl'))[-150:]
    if len(df) < 150:
        continue
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    if i > 10:
        break

cerebro.broker.setcash(100000.0)
# cerebro.run()


# cerebro = bt.Cerebro(stdstats=False)
# cerebro.broker.set_coc(True)

# spy = bt.feeds.YahooFinanceData(dataname='SPY',
#                                  fromdate=datetime(2012,2,28),
#                                  todate=datetime(2018,2,28),
#                                  plot=False)
# cerebro.adddata(spy)  # add S&P 500 Index

# for ticker in tickers:
#     df = pd.read_csv(f"survivorship-free/{ticker}.csv",
#                      parse_dates=True,
#                      index_col=0)
#     if len(df) > 100: # data must be long enough to compute 100 day SMA
#         cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=False))

cerebro.addobserver(bt.observers.Value)
cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0)
cerebro.addanalyzer(bt.analyzers.Returns)
cerebro.addanalyzer(bt.analyzers.DrawDown)
cerebro.addstrategy(TestStrategy)

print("Started Running Strategy")
results = cerebro.run()

# print(f"Sharpe: {results[0].analyzers.sharperatio.get_analysis()['sharperatio']:.3f}")
# print(f"Norm. Annual Return: {results[0].analyzers.returns.get_analysis()['rnorm100']:.2f}%")
# print(f"Max Drawdown: {results[0].analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")
# cerebro.plot()[0][0]
import pdb;pdb.set_trace()