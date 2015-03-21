/home/ann/rbm10/readme.txt

The files in this folder are related to an algorithm named RBM to predict pctlead of GSPC.

I found sklearn RBM documented here:

http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html

I think it is easy to interact with the API.

Currently the X-vectors I feed to GBRT and Logistic Regression are continuous numeric numbers.

Then the Y-vector is either booleans or numbers depending on whether I want to classify or regress.

It appears that RBM here wants the X-vectors to be booleans.

Here is a visualization of my current data:


dan@pav /home/ann/rbm10 $ 
dan@pav /home/ann/rbm10 $ 
dan@pav /home/ann/rbm10 $ head ftrGSPC2.csv 
cdate,cp,pctlead,pctlag1,pctlag2,pctlag4,pctlag8
2015-03-18,2099.500,0.000,1.216,0.880,1.624,1.363
2015-03-17,2074.280,1.216,-0.332,1.017,1.668,-1.274
2015-03-16,2081.190,-0.332,1.353,0.738,1.812,-0.826
2015-03-13,2053.400,1.353,-0.607,0.645,-1.252,-2.580
2015-03-12,2065.950,-0.607,1.260,1.066,-0.256,-2.429
2015-03-11,2040.240,1.260,-0.192,-1.885,-2.894,-3.053
2015-03-10,2044.160,-0.192,-1.696,-1.308,-2.591,-3.154
2015-03-09,2079.430,-1.696,0.394,-1.029,-1.345,-1.629
2015-03-06,2071.260,0.394,-1.417,-1.299,-2.179,-2.090
dan@pav /home/ann/rbm10 $ 
dan@pav /home/ann/rbm10 $ 
dan@pav /home/ann/rbm10 $ 

In the above table, the response variable is pctlead.

The X-columns are: pctlag1,pctlag2,pctlag4,pctlag8

Maybe I need to figure out how to transform each of the above columns into Boolean vectors?

If true, one obvious way to do that is to build a histogram for each column.

Maybe each histogram would have 10 buckets.

Then maybe I should build a Boolean vector which describes which bucket holds my numeric value.

So if pctlag1 = -1.1 maybe the corresponding vector would look like this:
[0,0,0,0,1,0,0,0,0,0]

I'd welcome any ideas on how to connect this RBM API from sklearn with ftrGSPC2.csv 

Dan
