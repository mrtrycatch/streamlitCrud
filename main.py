from cgitb import text
from multiprocessing import Value
from os import write
from turtle import onclick, onscreenclick
from typing import List
from numpy.core.fromnumeric import size
import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente


Page_cliente = st.sidebar.selectbox(
    'Cliente', ['Incluir', 'Consultar'], 0)

if Page_cliente == 'Consultar':
    PageListCliente.List()

if Page_cliente == 'Incluir':
    st.experimental_set_query_params()
    PageCreateCliente.Create()
    
