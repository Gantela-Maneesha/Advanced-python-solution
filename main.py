import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Data Analysis Dashboard")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Dataset")
    st.write(df)

    st.subheader("Statistics")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        column = st.selectbox("Select Column", numeric_columns)

        fig, ax = plt.subplots()
        ax.hist(df[column])

        st.pyplot(fig)