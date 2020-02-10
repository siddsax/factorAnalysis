import pandas as pd
import glob
import os
import numpy as np
from scipy.stats import linregress
from utils import *
import pickle
path = 'Data'

stocks = [pth.split('/')[-1][:-4] for pth in glob.glob(os.path.join(path,'*.pkl'))]

best, momentums,atrs = getBestMomentum(stocks, 10)
import pdb;pdb.set_trace()