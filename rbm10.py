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

# I should declare some integers to help me navigate the Arrays.

cdate_i   = 0
cp_i      = 1
pctlead_i = 2
x1_i      = 3
x2_i      = 4
x3_i      = 5
x4_i      = 6

# sklearn likes numpy arrays. I should convert my dataframe to array:
wide_a = np.array(df1)

# I should separate columns into x, y columns:
x_a    = wide_a[:,x1_i:x4_i]
y_a    = wide_a[:,pctlead_i]

import sklearn.neural_network

pdb.set_trace()
rbm1 = sklearn.neural_network.BernoulliRBM(n_components=2)
rbm1.fit(x_a, y_a)
