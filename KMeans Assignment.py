#FE 595A
#K Means Elbow Assignment

from sklearn.cluster import KMeans
from sklearn import datasets
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = datasets.load_iris()
x = iris.data[:, :2] #we only need first 2 features



wcss = []

for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# Creating Line Graph
plt.plot(range(1, 10), wcss)
plt.title('KMeans Elbow')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  # within cluster sum of squares
plt.show()














