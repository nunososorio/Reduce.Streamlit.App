import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA
import streamlit as st


def random_n(min_value=0, max_value=1000):
    return random.randint(min_value, max_value)

random.seed(42)

def write():
    st.markdown('''
    # Principal Component Analys on 2D data
    This demo lets you visualize the principal components obtained from 2D data. The data is a vector X of numbers between 1 and 99, and a vector Y equal to X plus some noise.
    - Use the slider below to change the level of noise!
    ''')
    # Display a loading warning
    with st.spinner('Please wait while the plots are being generated...'):
        
        col1_s, col2_s,col3_s = st.columns(3)
        
        # Pick a level of randomness
        with col1_s:
            noise_level=st.slider('', 
                      min_value=0.0, 
                      max_value=1.0, 
                      value=1.0, 
                      step=0.05, 
                      disabled=False, 
                      label_visibility="visible",
                      )

        col1, col2,col3 = st.columns(3)    
        with col1:
            st.markdown('''
            As you lower the noise level, the two variables will become more and more correlated. As a consequence, more and more of the variance can be explained by a single *Principal Component* (PC).
            If you lower the slider to 0, all the information of X and Y can be contained in a single vector, because knowing either X or Y will give you also the values of the other vector.
            - See how the PCs change in size and alignment with the data! 
            ''')
        with col2:
            st.markdown('''
            The plot below shows the fraction of the variance in the data that is explained by each of the components. When the noise is low, most of the changes in the data happen in one direction. Projecting the data onto a single vector along this direction can explain most of the variance. But when the noise increases, there is more and more changes along a second direction perpendicular to the first one. Then the changes cannot be reflected by a single vector.
            - See the changes when you move the slider! 
            ''')

        col1_p, col2_p,col3_p = st.columns(3)  
        
        with col1_p:
            # Generate data
            ## One vector X of number from 1 to 100
            x=np.random.choice(range(1,100), size=1000, replace=True)
            ## Once vector Y that combines X and a random number from to 99 in 
            ## proportions given by the noise level
            y=[random.random()*max(x)*noise_level + (1-noise_level)*i for i in x]

            # Place the data in a dataframe
            df=pd.DataFrame([x,y]).transpose()
            df.columns=['X','Y']

            # run PCA
            pca = PCA(n_components=2)
            principalComponents = pca.fit_transform(df )
            proj = pd.DataFrame(data = principalComponents, columns=['PC1','PC2'])

            # Plot
            ## First a scatter with the data
            fig = px.scatter(df, x='X', y='Y', opacity=.5)

            scale1=pca.explained_variance_ratio_[0]*80
            x1=[50,pca.components_[0][0]*scale1+50]
            y1=[50,pca.components_[0][1]*scale1+50]
            line_trace1 = go.Scatter(
                x=x1,
                y=y1,
                mode='lines',
                line=dict(color='red', width=6),  # Line color and width
                name='PC1'  # Legend label for the line
            )
            fig.add_trace(line_trace1)

            scale2=pca.explained_variance_ratio_[1]*80
            x2=[50,pca.components_[1][0]*scale2+50]
            y2=[50,pca.components_[1][1]*scale2+50]
            line_trace2 = go.Scatter(
                x=x2,
                y=y2,
                mode='lines',
                line=dict(color='green', width=6),  # Line color and width
                name='PC2'  # Legend label for the line
            )       
            fig.add_trace(line_trace2)

            # Adjust the figure
            fig.update_layout(
                font=dict(size=18)  # Adjust the font size as needed
            )
            fig.update_layout(height=800)
            fig.update_layout(width=800)

            st.plotly_chart(fig, use_container_width=True)
            

        with col2_p:  
            df_var=pd.DataFrame(pca.explained_variance_ratio_,columns=['Variance explained'])#.transpose()
            df_var['Component']=['PC1','PC2']

            fig2 = px.bar(df_var, y='Variance explained',x='Component',
                  opacity=.7)

            fig2.update_layout(height=800)
            fig2.update_layout(width=800)
            st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown(" © 2023 Nuno S. Osório, Leonardo D. Garma - Email: nosorio@med.uminho.pt | Leonardo Garma - Email: leonardo.garma@cnio.eski.se")
