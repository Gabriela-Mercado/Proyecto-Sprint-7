import pandas as pd
import plotly.express as px
import streamlit as st
carros_data = pd.read_csv('vehicles_us.csv')
st.header('Gran Venta de Vehículos')
hist_button = st.button('Ve una estadística en  histograma')
if hist_button:
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(carros_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
grafic_button = st.button('Ve una estadística en gráfico de dispersión')   
if grafic_button:
    st.write('Gráfico de dispersión para el conjunto de datos del kilometraje y cilindraje de los carros en venta')
    fig = px.scatter(carros_data, x="odometer", y="cylinders")
    st.plotly_chart(fig, use_container_width=True)