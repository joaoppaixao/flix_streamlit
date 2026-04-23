import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

reviews = [
    {
        'id': 1,
        'stars': 4
    },
    {
        'id': 2,
        'stars': 5
    },
    {
        'id': 3,
        'stars': 4
    },
]

def show_reviews():
    st.write('Lista de Reviews:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        enableSorting=True,
        key='reviews_grid',
    )
