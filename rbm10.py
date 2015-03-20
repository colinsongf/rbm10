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

# My data is sorted by cdate descending.
# Most recent row is row-zero.

# I should separate rows into train and oos:

oos_start   = 0
oos_end     = 10
train_start = oos_end + 1
train_end   = train_start + 1000

x_oos   = x_a[oos_start:oos_end]
y_oos   = y_a[oos_start:oos_end]
x_train = x_a[train_start:train_end]
y_train = y_a[train_start:train_end]

# ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html
import sklearn.neural_network

pdb.set_trace()
rbm1 = sklearn.neural_network.BernoulliRBM(n_components=2)

# ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.fit
rbm1.fit(x_train, y_train)

# ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.score_samples 	
# Compute the pseudo-likelihood of X.
rbm1.score_samples(x_oos)

# TypeError: ufunc 'logaddexp' not supported for the input types, 
# and the inputs could not be safely coerced to any supported types 
# according to the casting rule ''safe''

'bye'
