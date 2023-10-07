import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_s_curve
from sklearn.manifold import TSNE
import umap
from mpl_toolkits.mplot3d import Axes3D
import random

def random_n(min_value=0, max_value=1000):
    return random.randint(min_value, max_value)

def write():
    # Title and subtitle
    st.title("Reduce.Streamlit.App")
    st.markdown('''
    This part of the application provides an interactive visualization of dimensionality reduction techniques applied to a dataset with three dimensions. The dataset could represent, for example, the expression of three different genes, with each dot representing one of 1000 cells.
    The dimensionality reduction methods used in this application are PCA, t-SNE, and UMAP. PCA is a linear method, while t-SNE and UMAP are non-linear methods.
    In the visualizations, two points in the original data and in the reduced representations are connected by lines. One line is green and the other is red. These lines allow you to evaluate how well each method retains the distance between the cells. 
    ''')
    # Display a loading warning
    with st.spinner('Please wait while the plots are being generated...'):
        # Create a 3D dataset
        X, color = make_s_curve(n_samples=1000)

        # Apply PCA
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)

        # Apply t-SNE
        tsne = TSNE(n_components=2, random_state=42)
        X_tsne = tsne.fit_transform(X)

        # Apply UMAP
        reducer = umap.UMAP(random_state=42)
        X_umap = reducer.fit_transform(X)

        # Points for the GREEN line
        green_pointC = random_n()
        green_pointD = random_n()

        # Calculate the absolute difference between all color values
        color_diffs = np.abs(color[:, None] - color)

        # Set the diagonal to a large value to ignore self-differences
        np.fill_diagonal(color_diffs, np.inf)

        # Find the indices of the two points with the smallest color difference
        red_pointA, red_pointB = np.unravel_index(np.argmin(color_diffs), color_diffs.shape)

        # Plot the results
        fig, axs = plt.subplots(4, 1, figsize=(10, 50))

        # Original Data
        axs[0] = fig.add_subplot(411, projection='3d')
        axs[0].scatter(X[:, 0], X[:, 1], X[:, 2], c=color)
        axs[0].plot(*zip(X[green_pointC], X[green_pointD]), color='green', label='Green line')  
        axs[0].plot(*zip(X[red_pointA], X[red_pointB]), color='red', label='Red line')  
        axs[0].set_title('Original Data')

        # PCA
        axs[1] = fig.add_subplot(412)
        axs[1].scatter(X_pca[:, 0], X_pca[:, 1], c=color)
        axs[1].plot(*zip(X_pca[green_pointC], X_pca[green_pointD]), color='green')  
        axs[1].plot(*zip(X_pca[red_pointA], X_pca[red_pointB]), color='red')  
        axs[1].set_title('PCA')

        # t-SNE
        axs[2] = fig.add_subplot(413)
        axs[2].scatter(X_tsne[:, 0], X_tsne[:, 1], c=color)
        axs[2].plot(*zip(X_tsne[green_pointC], X_tsne[green_pointD]), color='green')  
        axs[2].plot(*zip(X_tsne[red_pointA], X_tsne[red_pointB]), color='red')  
        axs[2].set_title('t-SNE')

        # UMAP
        axs[3] = fig.add_subplot(414)
        axs[3].scatter(X_umap[:, 0], X_umap[:, 1], c=color)
        axs[3].plot(*zip(X_umap[green_pointC], X_umap[green_pointD]), color='green')  
        axs[3].plot(*zip(X_umap[red_pointA], X_umap[red_pointB]), color='red')  
        axs[3].set_title('UMAP')

        plt.tight_layout()
        st.pyplot(fig)
    st.markdown('''You might notice that the linear method (PCA) might not retain the distance as well as the non-linear methods (t-SNE and UMAP). This limitation might be more visible in the red line than the green line. Why do you think this is the case?
    Each time you reload the page, different lines are generated, allowing you to explore the behavior of these dimensionality reduction methods.
    Please note that the plots take a few seconds to load due to the computational complexity of the dimensionality reduction methods.''')
    st.markdown(" © 2023 Nuno S. Osório, Leonardo D. Garma - Email: nosorio@med.uminho.pt | Leonardo Garma - Email: leonardo.garma@cnio.eski.se")
