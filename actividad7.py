
import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)
temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
  if 7<pH or 6>pH:
    resultado=("Revisar pH")
  else:
      if 20>temperatura or temperatura>25:
          resultado=("revisar temperatura")
      else:
          resultado=("lote aceptable")
    # Completa aquí la lógica

        st.write(f"Resultado: {resultado}")
