
import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=7.5
)
temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
  if 7<pH or 6>pH:
    st.write("Revisar pH")

    # Completa aquí la lógica

    st.write(f"Resultado: {resultado}")
