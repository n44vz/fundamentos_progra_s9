import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"

st.title("Exploración de Pinguinos")

pinguinos = pd.read_csv(url)

if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(pinguinos)

especies = pinguinos['species'].unique()

seleccion = st.selectbox("Seleccione una especie:", especies)

pinguinos_filtrado = pinguinos[pinguinos['species'] == seleccion]

st.write(f"Estamos viendo los datos de la especie: {seleccion}")

st.subheader("Masa Corporal por especie")
st.bar_chart(pinguinos_filtrado['body_mass_g'])

st.subheader("Relación Largo de Aleta vs Peso")
st.scatter_chart(data=pinguinos_filtrado, x='flipper_length_mm', y='body_mass_g')