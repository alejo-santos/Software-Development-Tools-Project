import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
try:
    vehicles = pd.read_csv("/workspaces/Software-Development-Tools-Project/vehicles_us.csv")
except FileNotFoundError:
    url = 'https://raw.githubusercontent.com/jouna227/Software-Development-Tools-Project/main/vehicles_us.csv'
    vehicles = pd.read_csv(url, index_col=0)

# Main title
st.title('Car Advertisement Dashboard')

# Header
st.header('Dataset Overview')

# Display dataset
st.write(vehicles)

# Checkbox to toggle the display of the histogram
if st.checkbox('Show Mileage Histogram'):
    st.header('Mileage Distribution')
    # Create a histogram of vehicle mileage
    fig_hist = px.histogram(vehicles, x='odometer', title='Mileage Distribution')
    st.plotly_chart(fig_hist)

# Checkbox to toggle the display of the scatter plot
if st.checkbox('Show Price vs. Mileage Scatter Plot'):
    st.header('Price vs. Mileage')
    # Create a scatter plot of price vs. mileage
    fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Price vs. Mileage')
    st.plotly_chart(fig_scatter)
