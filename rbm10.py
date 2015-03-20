# /home/ann/rbm10/rbm10.py

# Demo:
# cd /home/ann/rbm10/
# python rbm10.py

import pdb
import pandas as pd
import numpy  as np
import sys

df1 = pd.read_csv('ftrGSPC2.csv')

df1.head()

import sklearn.neural_network

pdb.set_trace()
rbm1 = sklearn.neural_network.BernoulliRBM
