
import plotly.express as px
import streamlit as st
import pandas as pd

df=pd.read_csv('Combined Data.csv')
df.drop('Unnamed: 0' , axis=1 , inplace=True)

st.set_page_config(layout='wide',
                  page_title='tips home page',
                  page_icon= '🪙'
)

st.sidebar.success('select page above')
x=st.sidebar.checkbox('show data' , True , key=1)
st.markdown('<h1 style= "text-align:center; color: cyan ;">Home Page for Dashboard</h1>', unsafe_allow_html= True)
col1, col2, col3 = st.columns([3,4,3])

with col2:
    if x :
        st.markdown('<h3 style="text-align: center; color : MediumAquaMarine;">Dataset</h3>', unsafe_allow_html=True)
        st.dataframe(df.copy(), 800, 500,hide_index=True)
