#Ken Sherman
#SKLearn Regression Practice

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
boston = datasets.load_boston()

df = pd.DataFrame(boston.data)

df["PRICE"] = boston.target

print (df.corr())

#the greatest correlation to Price is attribute 12 = -.737663
#LSTAT    % lower status of the population
#the least correlation to price is attribute 3 = .175260, but that is a binary variable so the least
#correlation is actually attribute 7 = .249929
#- DIS      weighted distances to five Boston employment centres

    















