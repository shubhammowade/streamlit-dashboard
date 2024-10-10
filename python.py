import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
uploaded_file = st.file_uploader("Choose a file", type=['xlsx'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    # Display the DataFrame for debugging
    st.write("Data Preview:", df.head())

    # Display column names for debugging
    st.write("Columns in the DataFrame:", df.columns)

    st.title("Sales Dashboard")

    # Top Sales by Order ID
    st.header("Top Sales by Order ID")
    if 'Order ID' in df.columns and 'Sales' in df.columns:
        top_sales_order = df.groupby('Order ID')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)
        fig1 = px.bar(top_sales_order, x='Order ID', y='Sales', title='Top 10 Sales by Order ID')
        st.plotly_chart(fig1)
    else:
        st.error("Columns 'Order ID' or 'Sales' not found in the uploaded file.")

    # Sales Trendline
    st.header("Sales Trendline")
    if 'Date' in df.columns and 'Sales' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        sales_trend = df.groupby('Date')['Sales'].sum().reset_index()
        fig2 = px.line(sales_trend, x='Date', y='Sales', title='Sales Trendline')
        st.plotly_chart(fig2)
    else:
        st.error("Columns 'Date' or 'Sales' not found in the uploaded file.")

    # Total Sales by each Product type
    st.header("Total Sales by Product Type")
    if 'Product Type' in df.columns and 'Sales' in df.columns:
        sales_by_product = df.groupby('Product Type')['Sales'].sum().reset_index()
        fig3 = px.area(sales_by_product, x='Product Type', y='Sales', title='Total Sales by Product Type')
        st.plotly_chart(fig3)
    else:
        st.error("Columns 'Product Type' or 'Sales' not found in the uploaded file.")

    # Total Sales by each Sales Channel
    st.header("Total Sales by Sales Channel")
    if 'Sales Channel' in df.columns and 'Sales' in df.columns:
        sales_by_channel = df.groupby('Sales Channel')['Sales'].sum().reset_index()
        fig4 = px.line_polar(sales_by_channel, r='Sales', theta='Sales Channel', line_close=True, title='Total Sales by Sales Channel')
        st.plotly_chart(fig4)
    else:
        st.error("Columns 'Sales Channel' or 'Sales' not found in the uploaded file.")

    # Total Sales by Region
    st.header("Total Sales by Region")
    if 'Region' in df.columns and 'Sales' in df.columns:
        sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
        fig5 = px.pie(sales_by_region, names='Region', values='Sales', hole=0.3, title='Total Sales by Region')
        st.plotly_chart(fig5)
    else:
        st.error("Columns 'Region' or 'Sales' not found in the uploaded file.")

    # Total Sales made by each Sales Person
    st.header("Total Sales by Sales Person")
    if 'Sales Person' in df.columns and 'Sales' in df.columns:
        sales_by_person = df.groupby('Sales Person')['Sales'].sum().reset_index()
        fig6 = px.bar(sales_by_person, x='Sales Person', y='Sales', title='Total Sales by Sales Person')
        st.plotly_chart(fig6)
    else:
        st.error("Columns 'Sales Person' or 'Sales' not found in the uploaded file.")
