import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {
        'id': 1,
        'name': 'Leonardo di Caprio'
    },
    {
        'id': 2,
        'name': 'Tom Holland'
    },
    {
        'id': 3,
        'name': 'The Rock'
    },
]

def show_actors():
    st.write('Lista de Atores/Atrizes:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        enableSorting=True,
        key='actors_grid',
    )

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')