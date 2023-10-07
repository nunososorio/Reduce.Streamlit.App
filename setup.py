from setuptools import setup, find_packages

setup(
    name='your-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.25',
        'numba',
        'umap-learn',
        'streamlit',
        'matplotlib',
        'scikit-learn',
        'pandas',
        'plotly.express',
    ],
)
