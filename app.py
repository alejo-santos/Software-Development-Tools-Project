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

# Filter by vehicle make
selected_make = st.selectbox('Select a Vehicle Make', vehicles['model'].unique())

# Filtered dataset based on selected make
filtered_vehicles = vehicles[vehicles['model'] == selected_make]

# Histogram of Price
st.header('Histogram of Models')

# Check if filtered_vehicles DataFrame is not empty
if not filtered_vehicles.empty:
    fig_price = px.histogram(vehicles, x='price')
    st.plotly_chart(fig_price)
else:
    st.write("No data available for the selected vehicle make.")

# Scatter Plot of Price vs. Mileage
st.header('Scatter Plot of Price vs. Mileage')
fig_scatter = px.scatter(vehicles, x='odometer', y='price', title='Price vs. Mileage')
st.plotly_chart(fig_scatter)

# Checkbox to toggle logarithmic scale for price
log_scale = st.checkbox('Use Logarithmic Scale for Price')
if log_scale:
    fig_scatter.update_yaxes(type="log")



