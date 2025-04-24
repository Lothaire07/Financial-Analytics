import streamlit.components.v1 as components
import streamlit as st

def render_navbar():
    st.markdown("""
    <style>
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 100;
        display: flex;
        justify-content: center;
        gap: 2rem;
        background-color: #f0f0f0;
        padding: 1rem 0;
        font-family: 'Segoe UI', sans-serif;
        font-weight: bold;
        border-bottom: 1px solid #ddd;
    }
    .navbar a {
        color: #444;
        text-decoration: none;
        padding: 0.5rem 1rem;
        transition: color 0.2s;
    }
    .navbar a:hover {
        color: goldenrod;
    }
    </style>

    <div class="navbar">
        <a href="/home" target="_self">Home</a>
        <a href="/gc" target="_self">Gold</a>
        <a href="/si" target="_self">Silver</a>
        <a href="/cu" target="_self">Copper</a>
        <a href="/ax" target="_self">Aluminum</a>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar_nav():
    components.html("""
    <style>
    .sidebar-nav {
      position: fixed;
      top: 150px;
      right: 40px;
      background: rgba(255,255,255,0.9);
      padding: 1em;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      font-family: sans-serif;
      font-size: 14px;
    }

    .sidebar-nav a {
      display: block;
      margin: 0.5em 0;
      text-decoration: none;
      color: #444;
    }

    .sidebar-nav a:hover {
      color: goldenrod;
    }
    </style>

    <div class="sidebar-nav">
      <a href="#overview">Overview</a>
      <a href="#kpi">KPI</a>
      <a href="#chart">Chart</a>
      <a href="#insights">Insights</a>
    </div>
    """, height=300)


def hide_streamlit_elt():
    st.markdown("""
    <style>
    /* Cacher la sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    div[data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    button[data-testid="stBaseButton-headerNoPadding"] {
        display: none !important;
    }

    /* Étendre la page au maximum */
    div[data-testid="stAppViewContainer"] > div:first-child {
        width: 100%;
    }

    /* Cacher complètement le bouton Deploy + l’espace qu’il occupe */
    [data-testid="stAppDeployButton"] {
        display: none !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Enlève tout espace ajouté par le header Streamlit */
    header[data-testid="stHeader"] {
        height: 0 !important;
        visibility: hidden !important;
    }

    /* Supprimer le padding par défaut de la page */
    .block-container {
        padding-top: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

### def hide_deploy(): ### To hide the deploy function when testing
