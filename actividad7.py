
import streamlit as st
st.sidebar.title("Actividad7")
st.sidebar.write("Audric Gómez",         
                 "3°L",
                 "Facultad de ciencias quimicas")
st.title("Evaluación de un lote")
resultado=0
pH = st.number_input(
    "pH",
    value=6.5
)
temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)
concentracion = st.number_input(
    "Concentración (%)",
    value=10.0
)
if st.button("Evaluar"):
  if 7<pH or 6>pH:
    resultado=("Revisar pH")
  elif 8>concentracion or concentracion>12:
      resultado=("revisar concentración")
  else:
      if 20>temperatura or temperatura>25:
          resultado=("revisar temperatura")
      else:
          resultado=("lote aceptable")
  st.write(f"Resultado: {resultado}")
else:
    st.write("aun no se evalua")

