from numpy import True_
import streamlit as st

from pages.about import about_page

about_page = st.Page(
    page="pages/About.py",
    title="Devs",
    icon="👩‍💻",
)

stock_page = st.Page(
    page="pages/stockVisualize.py",
    title="Stock Visualzer",
    icon="📈",
    default=True,
)

world_pop = st.Page(
    page="pages/worldPopVisual.py",
    title="World Population",
    icon="🌍",
)

user_data = st.Page(
    page="pages/visualizeUserData.py",
    title="Visualize Your Data",
    icon="👤",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [stock_page, world_pop, user_data],
    }
)

st.sidebar.text("Made by grishrana and Sushil346")

pg.run()
