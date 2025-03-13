import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import warnings

if __name__ == "__main__":

    warnings.simplefilter('ignore')

    n_clusters = 3
    seed = 12345

    data_arr_2d = np.loadtxt("test2D.txt")

    gmm = GaussianMixture(n_components=n_clusters, random_state=seed)
    gmm.fit(data_arr_2d)
    labels = gmm.predict(data_arr_2d)

    plt.scatter(data_arr_2d[:, 0], data_arr_2d[:, 1], c=labels, cmap='viridis', edgecolors='k')
    plt.scatter(gmm.means_[:, 0], gmm.means_[:, 1], c='red', marker='x', s=100, label='Centroids')
    plt.legend()
    plt.title("Gaussian Mixture Model Clustering")
    plt.show()
    sys.exit(0)
