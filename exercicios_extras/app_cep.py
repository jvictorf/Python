import streamlit as st
import requests
import pandas as pd

URL = "https://cep.awesomeapi.com.br/json/{cep}"

st.title("Busca CEP")

cep = st.text_input("Busque seu cep: ")

if cep != "":
    resp = requests.get(URL.format(cep=cep))
    data  = pd.DataFrame([resp.json()])
    st.dataframe(data)