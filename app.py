import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
vehicles = pd.read_csv("/workspaces/Software-Development-Tools-Project/vehicles_us.csv")

# Main title
st.title('Car Advertisement Dashboard')

# Header
st.header('Dataset Overview')

# Display dataset
st.write(vehicles)

# Histogram of Price
st.header('Histogram of Price')
fig_price = px.histogram(vehicles, x='price')
st.plotly_chart(fig_price)

# Scatter Plot of Price vs. Mileage
st.header('Scatter Plot of Price vs. Mileage')
fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Price vs. Mileage')
st.plotly_chart(fig_scatter)

# Checkbox to toggle logarithmic scale for price
log_scale = st.checkbox('Use Logarithmic Scale for Price')
if log_scale:
    fig_scatter.update_yaxes(type="log")



