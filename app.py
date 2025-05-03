# app.py
import streamlit as st

import home
from pages.agricultural import zc, zl, zm, zo, zs
from pages.metals import si, gc, ax, hg, pa, pl

# etc.
# Faire une map , faut que je me fasse epxliquer
PAGES = {
    "home": home.render,
    "gc": gc.render,
    "si": si.render,
    "ax": ax.render,
    "hg": hg.render,
    "pa": pa.render,
    "pl": pl.render,
    "zc": zc.render,
    "zl": zl.render,
    "zm": zm.render,
    "zo": zo.render,
    "zs": zs.render,

    # ...
}

page = st.query_params.get("page", "home")

if page in PAGES:
    PAGES[page]()
else:
    st.title("Welcome Home")
    st.write("Select a page.")