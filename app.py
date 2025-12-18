import streamlit as st
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Polars EDA Tool", layout="wide")

st.title("🚀 Polars-Powered Exploratory Data Analysis")
st.write("Robust EDA tool that handles **real-world dirty Kaggle CSVs**")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        # ---------- TRY POLARS (FAST PATH) ----------
        df = pl.read_csv(
            uploaded_file,
            infer_schema_length=20000,
            truncate_ragged_lines=True
        )
        st.success("Loaded using Polars 🚀")

    except Exception:
        # ---------- FALLBACK TO PANDAS ----------
        st.warning("Malformed CSV detected. Using pandas fallback...")

        uploaded_file.seek(0)

        pdf = pd.read_csv(
            uploaded_file,
            engine="python",
            on_bad_lines="skip"
        )

        df = pl.from_pandas(pdf)
        st.success("Loaded using Pandas → Converted to Polars ✅")

    # ---------- DATASET OVERVIEW ----------
    st.subheader("📌 Dataset Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("🧬 Schema")
    st.code(df.schema)

    # ---------- PREVIEW ----------
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(20).to_pandas())

    # ---------- DESCRIPTIVE STATS ----------
    st.subheader("📊 Descriptive Statistics")
    st.dataframe(df.describe().to_pandas())

    # ---------- MISSING VALUES ----------
    st.subheader("❌ Missing Values")
    missing = df.select(pl.all().null_count())
    st.dataframe(missing.to_pandas())

    # ---------- NUMERIC COLUMNS ----------
    numeric_cols = [
        col for col, dtype in df.schema.items()
        if dtype in [pl.Int64, pl.Float64]
    ]

    if numeric_cols:
        # ---------- CORRELATION ----------
        st.subheader("📈 Correlation Matrix")
        corr = df.select(numeric_cols).corr().to_pandas()

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        # ---------- DISTRIBUTION ----------
        st.subheader("📉 Distribution Plot")
        selected_col = st.selectbox("Select numeric column", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col].drop_nulls().to_list(), bins=30)
        ax.set_title(f"Distribution of {selected_col}")
        st.pyplot(fig)

    # ---------- GROUP BY ----------
    st.subheader("🧮 Group By Analysis")
    group_col = st.selectbox("Select grouping column", df.columns)

    if numeric_cols:
        agg_col = st.selectbox("Select numeric column to aggregate", numeric_cols)

        grouped = df.group_by(group_col).agg(
            pl.col(agg_col).mean().alias("Mean"),
            pl.col(agg_col).sum().alias("Sum"),
            pl.count().alias("Count")
        )

        st.dataframe(grouped.to_pandas())

    # ---------- FOOTER ----------
    st.info(
        "⚡ Built with **Polars** for speed and **pandas fallback** for real-world CSV robustness."
    )
