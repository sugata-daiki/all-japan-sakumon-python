import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

if __name__ == "__main__":
    data_arr_100d = np.loadtxt("test100d.txt")
    pca = PCA(n_components=2)
    data_arr_100d_pca = pca.fit_transform(data_arr_100d)

    plt.scatter(data_arr_100d_pca[:, 0], data_arr_100d_pca[:, 1], alpha=0.7)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA Dimensionality Reduction")
    plt.show()

    print("Explained Variance Ratio:", pca.explained_variance_ratio_)
