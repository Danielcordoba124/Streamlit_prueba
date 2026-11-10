import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Población Mundial", layout="wide")
st.title("Análisis de la población mundial")
st.write("Los 10 países más poblados del mundo")

archivo = st.file_uploader("Seleccione el archivo CSV", type="csv")

if archivo:
  datos = pd.read_csv(archivo)
  top10 = datos.sort_values("2022 Population", ascending=False).head(10)

  # Mostrar la tabla limpia
  st.dataframe(
      top10[["Country/Territory", "2015 Population", "2020 Population", "2022 Population"]]
  )

  poblacion_2015 = top10["2015 Population"].to_numpy()

  poblacion_total_2015 = np.sum(poblacion_2015)
  promedio = np.mean(poblacion_2015)
  mediana = np.median(poblacion_2015)
  maximo = np.max(poblacion_2015)
  minimo = np.min(poblacion_2015)

  st.subheader("Estadísticas de la población en 2015")
  c1, c2, c3, c4, c5 = st.columns(5)
  c1.metric("Población total:", f"{poblacion_total_2015/1000000:.2f}", "Millones")
  c2.metric("Promedio:", f"{promedio/1000000:.2f}", "Millones")
  c3.metric("Mediana:", f"{mediana/1000000:.2f}", "Millones")
  c4.metric("Máximo:", f"{maximo/1000000:.2f}", "Millones")
  c5.metric("Mínimo:", f"{minimo/1000000:.2f}", "Millones")

  st.subheader("Comparación de la población por país (en Millones)")
  grafico = (
      top10.set_index("Country/Territory")[
          ["2015 Population", "2020 Population", "2022 Population"]
      ]
      / 1000000
  )
  st.bar_chart(grafico)

  st.subheader("Datos de los países")
  st.dataframe(grafico)

else:
  st.write("Ingrese un Dataset")
