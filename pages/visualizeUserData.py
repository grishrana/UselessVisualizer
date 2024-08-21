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


def corr_map(df):
    corr = df.corr(numeric_only=True)
    corr_masked = corr.where(np.identity(len(corr.columns)).astype(bool))
    fig, axe = plt.subplots(figsize=(10, 10))
    sns.heatmap(data=corr_masked, annot=True, fmt=".1f", ax=axe)
    return fig


def scatter_plot(df, col1, col2):
    fig, axe = plt.subplots(figsize=(10, 10))
    axe.scatter(df[col1], df[col2])
    axe.set(title=f"{col1} vs {col2}", xlabel=f"{col1}", ylabel=f"{col2}")
    return fig


def line_plot(df, col):
    fig, axe = plt.subplots(figsize=(10, 10))
    axe.plot(range(len(df[col])), df[col].sample(frac=1).values, ":g")
    axe.set(title=f"Line plot of {col}")
    return fig


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

    if len(numeric_columns) >= 2:

        st.subheader("Correlation Heatmap")
        heatmap = corr_map(df)
        st.pyplot(heatmap)

        col1, col2 = random.sample(list(numeric_columns), 2)

        st.subheader(f"Scatter Plot {col1} vs {col2}")
        scatter = scatter_plot(df, col1, col2)
        st.pyplot(scatter)

    else:
        st.error("Not enough numerical Columns")

    if len(numeric_columns) > 0:
        col = random.choice(list(numeric_columns))

        st.header(f"Line Plot of {col}")
        line = line_plot(df, col)
        st.pyplot(line)

    else:
        st.error("Not enough numerical columns")

else:
    st.session_state.uploaded_file = None
