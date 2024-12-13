
import plotly.express as px
import streamlit as st
import pandas as pd


st.set_page_config(layout='wide',
                  page_title='tips',
                  page_icon= '🪙'
)

tab1 , tab2 =st.tabs(['📈 Describtive Statics','📊 Charts'])

df=pd.read_csv('Combined Data.csv')
df.drop('Unnamed: 0' , axis=1 , inplace=True)
num=df.describe()
cat=df.describe(include='O')
color1= px.colors.qualitative.Pastel


with tab1:
    col1 , col2 , col3 = st.columns([6,0.5,6])
    
    with col1:
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(num.T, 700, 150)

    with col3:
            st.subheader('Categorical Describtive Statistics')
            st.dataframe(cat.T, 500, 200)


with tab2:

    with st.container():
        col1,col2,col3=st.columns([4,5,4])
    

        new_def1=df.groupby('product_type').agg({'total_price':'mean'}).sort_values(by='product_type')
        fig1=px.bar(new_def1 , y='total_price'  , title='the average of sales for each product' , color_discrete_sequence=color1)
        col1.plotly_chart(fig1)

        new_def2=df.groupby('order_month_name').agg({'total_price':'mean'}).sort_values(by='order_month_name')
        fig2=px.scatter(new_def2 , y='total_price' , title='the amount of sales among months' , color_discrete_sequence=color1)
        col1.plotly_chart(fig2)


        new_def3=df.groupby('order_day_name').agg({'total_price':'mean'}).sort_values(by='order_day_name')
        fig3=px.scatter(new_def3 , y='total_price' , title='the amount of sales among days' , color_discrete_sequence=color1)
        col1.plotly_chart(fig3)


        new_def4=df.groupby('gender').agg({'total_price':'mean'}).sort_values(by='gender')
        fig4=px.line(new_def4 , y='total_price' , title='the average of sales for each gender' , color_discrete_sequence=color1)
        col1.plotly_chart(fig4)

        new_def5=df.groupby('customer_name')[['order_id']].count().sort_values(by='customer_name').head(10)
        fig5=px.bar(new_def5 , y='order_id' , title='the  number of orders placed by top 10 customers' , color_discrete_sequence=color1)
        col2.plotly_chart(fig5)

        new_def6=df.groupby('customer_name')[['total_price']].mean().sort_values(by='customer_name').head(10)
        fig6=px.bar(new_def6 , y='total_price' , title='top 10 customers had spent the most money' , color_discrete_sequence=color1)
        col2.plotly_chart(fig6)

        new_def7=df.groupby('age')[['total_price']].mean().sort_values(by='age').head(10)
        fig7=px.line(new_def7 , y='total_price' , title='top 10 ages paid most money in products' , color_discrete_sequence=color1)
        col2.plotly_chart(fig7)

        new_def8=df.groupby('state')[['total_price']].mean().sort_values(by='state')
        fig8=px.bar(new_def8 , y='total_price' , title='the average of sales for each state' , color_discrete_sequence=color1)
        col2.plotly_chart(fig8)

        new_def9=df.groupby('order_month_name')[['order_id']].count().sort_values(by='order_month_name')
        fig9=px.line(new_def9 , y='order_id' , title='the trend of total numbers of orders among the months' , color_discrete_sequence=color1)
        col2.plotly_chart(fig9)

        new_def10=df.groupby('product_type')[['quantity_x']].sum().sort_values(by='product_type')
        fig10=px.bar(new_def10 , y='quantity_x' , title='the total number of products sold by each product type' , color_discrete_sequence=color1)
        col3.plotly_chart(fig10)

        new_def11=df.groupby('product_type')[['price_per_unit']].mean().sort_values(by='product_type')
        fig11=px.bar(new_def11 , y='price_per_unit' , title='the average price per unit of each product' , color_discrete_sequence=color1)
        col3.plotly_chart(fig11)

        new_def12=df.groupby('order_day_name')[['order_id']].count().sort_values(by='order_day_name')
        fig12=px.line(new_def12 , y='order_id' , title='trend total number of orders get placed amon days of the week' , color_discrete_sequence=color1)
        col3.plotly_chart(fig12)

        new_def13=df.groupby('size')[['total_price']].mean().sort_values(by='size').head(5)
        fig13=px.scatter(new_def13 , y='total_price' , title='trend top 5 product size over sales' , color_discrete_sequence=color1)
        col3.plotly_chart(fig13)



        
