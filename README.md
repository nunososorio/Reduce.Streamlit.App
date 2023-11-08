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

Garma, LD, Osório, NS. Demystifying dimensionality reduction techniques in the ‘omics’ era: A practical approach for biological science students. Biochem Mol Biol Educ. 2023. https://doi.org/10.1002/bmb.21800

BibTex:
```@article{https://doi.org/10.1002/bmb.21800,
author = {Garma, Leonardo D. and Osório, Nuno S.},
title = {Demystifying dimensionality reduction techniques in the ‘omics’ era: A practical approach for biological science students},
journal = {Biochemistry and Molecular Biology Education},
volume = {n/a},
number = {n/a},
pages = {},
keywords = {data science, dimensionality reduction, general education for science majors, Jupyter, original models for teaching and learning, PCA, postgraduate education, Python, teaching and learning techniques methods and approaches, t-SNE, UMAP},
doi = {https://doi.org/10.1002/bmb.21800},
url = {https://iubmb.onlinelibrary.wiley.com/doi/abs/10.1002/bmb.21800},
eprint = {https://iubmb.onlinelibrary.wiley.com/doi/pdf/10.1002/bmb.21800},
abstract = {Abstract Dimensionality reduction techniques are essential in analyzing large ‘omics’ datasets in biochemistry and molecular biology. Principal component analysis, t-distributed stochastic neighbor embedding, and uniform manifold approximation and projection are commonly used for data visualization. However, these methods can be challenging for students without a strong mathematical background. In this study, intuitive examples were created using COVID-19 data to help students understand the core concepts behind these techniques. In a 4-h practical session, we used these examples to demonstrate dimensionality reduction techniques to 15 postgraduate students from biomedical backgrounds. Using Python and Jupyter notebooks, our goal was to demystify these methods, typically treated as “black boxes”, and empower students to generate and interpret their own results. To assess the impact of our approach, we conducted an anonymous survey. The majority of the students agreed that using computers enriched their learning experience (67\%) and that Jupyter notebooks were a valuable part of the class (66\%). Additionally, 60\% of the students reported increased interest in Python, and 40\% gained both interest and a better understanding of dimensionality reduction methods. Despite the short duration of the course, 40\% of the students reported acquiring research skills necessary in the field. While further analysis of the learning impacts of this approach is needed, we believe that sharing the examples we generated can provide valuable resources for others to use in interactive teaching environments. These examples highlight advantages and limitations of the major dimensionality reduction methods used in modern bioinformatics analysis in an easy-to-understand way.}
}```

## License
This project is licensed under the terms of the MIT license. For more information, please see the LICENSE file.
