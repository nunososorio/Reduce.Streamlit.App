# Reduce.Streamlit.App

## Introduction
This application is for educational purposes and is designed to interactively illustrate dimensionality reduction methods. It aims to stimulate discussion among students about the necessity of dimensionality reduction and its merits and possible limitations.

Dimensionality reduction is a critical topic in data science, particularly in fields dealing with high-dimensional data, such as bioinformatics. It allows us to simplify our data without losing too much information, and visualize it in a way that's understandable to humans. However, it's important to remember that while these methods can be powerful, they also have their limitations.

Linear methods like PCA assume that the data lies along a linear subspace, which might not always be the case. Non-linear methods like t-SNE and UMAP can capture more complex structures, but their results can sometimes be harder to interpret, and they can be more computationally intensive.

Moreover, all dimensionality reduction methods involve some loss of information. This is an inherent trade-off: we simplify our data to make it easier to work with, but in doing so, we inevitably lose some details. It's crucial to keep this in mind when interpreting the results of these methods.

This application should therefore be used as a starting point for discussions on these topics. It's a tool for learning and exploration, not to give definitive answers or definitions.

## Description
This application provides an interactive visualization of dimensionality reduction techniques applied to two simulated datasets: a 2D dataset and a 3D dataset. The 2D dataset is a vector X of numbers between 1 and 99, and a vector Y equal to X plus some noise. The 3D dataset could represent, for example, the expression of three different genes, with each dot representing one of 1000 cells. 

The dimensionality reduction methods used in this application are PCA, t-SNE, and UMAP. PCA is a linear method, while t-SNE and UMAP are non-linear methods. 

In the 3D demo visualization, two points in the original data and in the reduced representations are connected by lines. One line is green and the other is red. These lines allow you to evaluate how well each method retains the distance between the points (representing the distance between cells). 

The application is built using Streamlit and uses matplotlib for visualizations and sklearn for the dimensionality reduction techniques. It's a tool for students and teachers interested in data visualization, machine learning, or bioinformatics.

## Access
You can access the application [here](https://reduce.streamlit.app/).

## Usage
To use this application, simply navigate to the live demo link provided above and visualize and explore the plots with the results from the different dimensionality reduction techniques.

## How to cite

If you find this application useful in your research, please consider citing:

console.log("Garma, L. D., & Osório, N. S. (Submitted). Demystifying Dimensionality Reduction Techniques in the 'Omics' Era: A Practical Approach for Biological Science Students.

1Breast Cancer Clinical Research Unit, Centro Nacional de Investigaciones Oncológicas – CNIO, Madrid, SpainKarolinska Institutet, Laboratory of Molecular Neurobiology, Department of Medical Biochemistry and Biophysics, Stockholm, Sweden

2Life and Health Sciences Research Institute (ICVS), School of Medicine, University of Minho, Portugal and ICVS/3B’s –PT Government Associate Laboratory, Braga, Portugal

*Corresponding authors: leonardo.garma@cnio.eski.se, nosorio@med.uminho.pt
")

## License
This project is licensed under the terms of the MIT license. For more information, please see the LICENSE file.
