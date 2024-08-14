import streamlit as st
import pandas as pd
import wbgapi as wb

pop_Data = None

st.title("**World Population Visualization**")


@st.cache_data
def getData(year_start=2020, year_end=2023) -> pd.DataFrame:
    df = wb.data.DataFrame("SP.POP.TOTL", time=range(year_start, year_end + 1))
    return df


year_start, year_end = st.select_slider(
    "Select the range of Years", value=(2020, 2023), options=range(1974, 2024)
)
if year_start == year_end:
    st.warning("Starting Year and Ending Year cannot be the same!!")

else:
    pop_Data = getData(year_start, year_end)

st.write(pop_Data)
