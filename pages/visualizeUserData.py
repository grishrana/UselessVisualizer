import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import random

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None


def read_file(userfile) -> pd.DataFrame:
    filename, fileext = os.path.splitext(userfile.name)
    if fileext == ".xlsx":
        df = pd.read_excel(userfile)
    elif fileext == ".csv":
        df = pd.read_csv(userfile)
    else:
        st.error("Invalid file format")
    return df


st.header("**Visualize Your Data**")
uploaded_file = st.file_uploader("Choose an Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file
    try:
        df = read_file(st.session_state.uploaded_file)
        st.write(df)
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

    numeric_columns = df.select_dtypes(include="number")

    st.subheader("**Correlation Heatmap**")
    corr = df.corr(numeric_only=True)  # pyright: ignore
    corr_masked = corr.where(
        np.identity(len(corr.columns)).astype(bool)
    )  # pyright: ignore
    fig, axe = plt.subplots(figsize=(10, 10))
    sns.heatmap(data=corr_masked, annot=True, fmt=".1f", ax=axe)

    st.pyplot(fig)

    if len(numeric_columns) >= 2:
        col1, col2 = random.sample(list(numeric_columns), 2)

        st.subheader(f"Scatter Plot {col1} vs {col2}")
        fig, ax = plt.subplots()
        ax.scatter(df[col1], df[col2])
        ax.set(title=f"{col1} vs {col2}", xlabel=f"{col1}", ylabel=f"{col2}")
        st.pyplot(fig)

    else:
        st.error("Not enough numerical Columns")

    if len(numeric_columns) > 0:
        col = random.choice(list(numeric_columns))

        st.header(f"Line Plot of {col}")
        fig, ax = plt.subplots()
        ax.plot(range(len(df[col])), df[col].sample(frac=1).values, ":g")
        ax.set(title=f"Line Plot of {col}")

        st.pyplot(fig)

    else:
        st.error("Not enough numerical columns")

else:
    st.session_state.uploaded_file = None
