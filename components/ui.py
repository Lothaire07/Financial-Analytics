import streamlit.components.v1 as components
import streamlit as st


def render_navbar():
    st.markdown(
        """
        <style>
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 999;
            display: flex;
            gap: 2rem;
            justify-content: center;
            background-color: #f0f0f0;
            padding: 1rem 0;
            font-family: 'Segoe UI', sans-serif;
            font-weight: bold;
            border-bottom: 1px solid #ddd;
            background: rgba(14, 17, 23, 0.75); /* fond sombre, partiellement transparent */
            backdrop-filter: blur(10px);        /* effet flou derrière */
            -webkit-backdrop-filter: blur(10px);
        }

        .navbar a {
            color: White;
            text-decoration: none;
            padding: 0.5rem 1rem;
            transition: color 0.3s ease;
            height: 32px;
            display: inline-flex; /*fix metals*/
            align-items: center;
            justify-content: center;
        }

        .navbar:hover {
            background: rgba(14, 17, 23, 0.95);
            transition: 0.3s;
        }
        .navbar a:hover {
            color: #94a3b8;
            text-shadow: 0 0 10px rgba(154, 165, 181, 0.8), 0 0 20px rgba(154, 165, 181, 0.6);
        }
        
    
        /* Dropdown */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: white;
            min-width: 160px;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
            z-index: 1000;
        }

        .dropdown-content a {
            display: block;
            padding: 0.5rem 1rem;
            color: #333;
            text-align: left;
            text-decoration: none;
            font-weight: normal;
        }

        .dropdown-content a:hover {
            background-color: #f3f3f3;
            color: goldenrod;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        /* Décale le contenu principal vers le bas */
        .block-container {
            padding-top: 100px !important;
        }
        </style>

        <div class="navbar">
        <a href="/" target="_self">Home</a>
        <div class="dropdown">
        <a href="#">Metals ▾</a>
        <div class="dropdown-content">
        <a href="/?page=gc" target="_self">Gold</a>
        <a href="/?page=si" target="_self">Silver</a>
        <a href="/?page=hg" target="_self">Copper</a>
        <a href="/?page=ax" target="_self">Aluminum</a>
        <a href="/?page=pa" target="_self">Palladium</a>
        <a href="/?page=pl" target="_self">Platinum</a>
        </div>
        </div>
        
        <div class="dropdown">
        <a href="#">Agricultural ▾</a>
        <div class="dropdown-content">
        <a href="/?page=zc" target="_self">Corn</a>
        <a href="/?page=zw" target="_self">Wheat</a>
        <a href="/?page=zs" target="_self">Soybeans</a>
        <a href="/?page=zl" href="/zm" target="_self">Soybean Meal</a>
        <a href="/?page=zo" target="_self">Oats</a>
        <!-- Ajoute plus de produits ici si nécessaire -->
        </div>
        </div>
        <a href="/energy" target="_self">Energy</a>
        <a href="/indices" target="_self">Indices</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_nav():
    components.html(
        """
        <style>
        .sidebar-nav-container {
            position: fixed;
            top: 0;
            right: 0;
            height: 100vh;
            width: auto;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            pointer-events: none;
            z-index: 9999;
        }

        .sidebar-nav {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 1rem;
            border-radius: 10px 0 0 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            font-family: 'Segoe UI', sans-serif;
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: auto;
            margin-right: 10px;
        }

        .sidebar-nav-container:hover .sidebar-nav {
            opacity: 1;
        }

        .sidebar-nav a {
            display: block;
            margin: 0.5rem 0;
            text-decoration: none;
            color: #d1d1d1;
            font-weight: 500;
            cursor: pointer;
            transition: color 0.3s ease, text-shadow 0.3s ease;
        }

        .sidebar-nav a:hover {
            color: #f5c518;
            text-shadow: 0 0 6px #f5c518;
        }

        html {
            scroll-behavior: smooth;
        }
        </style>

        <div class="sidebar-nav-container">
            <div class="sidebar-nav">
                <a onclick="document.getElementById('overview').scrollIntoView({ behavior: 'smooth' });">Overview</a>
                <a onclick="document.getElementById('kpi').scrollIntoView({ behavior: 'smooth' });">KPI</a>
                <a onclick="document.getElementById('chart').scrollIntoView({ behavior: 'smooth' });">Chart</a>
                <a onclick="document.getElementById('insights').scrollIntoView({ behavior: 'smooth' });">Insights</a>
            </div>
        </div>
        """,
        height=300,
    )

def hide_streamlit_elt():
    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )


### def hide_deploy(): ### To hide the deploy function when testing
