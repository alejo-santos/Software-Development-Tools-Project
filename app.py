import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
try:
    vehicles = pd.read_csv("/workspaces/Software-Development-Tools-Project/vehicles_us.csv")
except FileNotFoundError:
    url = 'https://raw.githubusercontent.com/jouna227/Software-Development-Tools-Project/main/vehicles_us.csv'
    vehicles = pd.read_csv(url)

# Main title
st.title('Car Advertisement Dashboard')

# Header
st.header('Dataset Overview')

# Display dataset
st.write(vehicles)

# Filter by vehicle make
selected_make = st.selectbox('Select a Vehicle Make', vehicles['model'].unique())
filtered_vehicles = vehicles[vehicles['model'] == selected_make]

# Histogram of Price
st.header('Histogram of Price')
fig_price = px.histogram(filtered_vehicles, x='price')
st.plotly_chart(fig_price)

# Scatter Plot of Price vs. Mileage
st.header('Scatter Plot of Price vs. Mileage')
fig_scatter = px.scatter(filtered_vehicles, x='odometer', y='price', title='Price vs. Mileage')
st.plotly_chart(fig_scatter)

# Checkbox to toggle logarithmic scale for price
log_scale = st.checkbox('Use Logarithmic Scale for Price')
if log_scale:
    fig_scatter.update_yaxes(type="log")
    st.plotly_chart(fig_scatter)