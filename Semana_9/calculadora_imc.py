import streamlit as st

st.title("Calculadora IMC")

st.sidebar.title("Bienvenido")
st.sidebar.header("Parámetros")
peso = st.sidebar.number_input("Peso (KG)", 30.0, 300.0,  value = 70.0)
estatura = st.sidebar.number_input("Estatura (CM)", 110.0, 250.0,  170.0)

if st.button("Calcular"):
    estatura_m = estatura / 100
    imc = peso / (estatura_m ** 2)
    st.metric(label="Su IMC es de:", value=f"{imc:.2f}")
    if imc < 25:
        st.success("Rango óptimo")
    else:
        st.warning("Atención!")