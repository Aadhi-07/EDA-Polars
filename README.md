# 🚀 Polars-Powered Exploratory Data Analysis (EDA) Tool

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Polars](https://img.shields.io/badge/Polars-Fast%20EDA-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![License](https://img.shields.io/github/license/Aadhi-07/EDA-Polars)
![Repo Size](https://img.shields.io/github/repo-size/Aadhi-07/EDA-Polars)
![Last Commit](https://img.shields.io/github/last-commit/Aadhi-07/EDA-Polars)

A **Streamlit-based Exploratory Data Analysis (EDA) web application** powered by **Polars**, built to handle **real-world, messy CSV datasets (including Kaggle datasets)** efficiently.  
The app prioritizes **Polars for speed** and automatically falls back to **pandas** when malformed CSV files are encountered.

---

## ✨ Features

- 📂 Upload CSV files directly from the browser
- ⚡ Fast CSV loading using **Polars**
- 🛡️ Automatic fallback to **pandas** for malformed or dirty CSVs
- 📌 Dataset overview (row & column count)
- 🧬 Schema inspection
- 🔍 Data preview (first 20 rows)
- 📊 Descriptive statistics
- ❌ Missing value analysis
- 📈 Correlation heatmap for numeric columns
- 📉 Distribution (histogram) plots
- 🧮 Group-by analysis with Mean, Sum, and Count
- 🌐 Interactive UI built using Streamlit

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Polars** – High-performance DataFrame library
- **Pandas** – Fallback for malformed CSV handling
- **Streamlit** – Web application framework
- **Matplotlib** – Data visualization
- **Seaborn** – Correlation heatmaps

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Aadhi-07/EDA-Polars.git
cd EDA-Polars
```
Install dependencies:
```bash

pip install -r requirements.txt
▶️ Running the Application
Start the Streamlit app using:
```
```bash

streamlit run app.py
Open your browser and navigate to:
```

http://localhost:8501
🖥️ Application Workflow
1️⃣ CSV Upload
Users upload a .csv file via the UI.

The application first attempts to load the file using Polars.

If Polars fails due to malformed data, the app automatically:

Loads the CSV using pandas

Converts it into a Polars DataFrame

2️⃣ Dataset Overview
Displays:

Total number of rows

Total number of columns

Shows the complete Polars schema of the dataset

3️⃣ Data Preview
Displays the first 20 rows of the dataset in tabular format

4️⃣ Statistical Analysis
Generates descriptive statistics using df.describe()

Displays missing value count for every column

5️⃣ Visual Analysis
Automatically detects numeric columns

Generates:

Correlation heatmap for numeric features

Histogram distribution plot for a selected numeric column

6️⃣ Group By Analysis
Allows selection of any column for grouping

Aggregates numeric columns using:

Mean

Sum

Count


```text

screenshots/
├── upload.png
├── preview.png
├── stats.png
├── correlation.png
├── distribution.png
└── groupby.png
```



📁 Project Structure
```text

EDA-Polars/
│
├── app.py               # Streamlit EDA application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── screenshots/         # Application screenshots
```
⚡ Why Polars?
Written in Rust for high performance

Multi-threaded execution

Faster than pandas for large datasets

Lower memory usage

Polars makes this project suitable for large-scale, real-world data analysis.

🎯 Use Cases
Exploratory Data Analysis (EDA)

Machine Learning preprocessing

Kaggle datasets analysis

Academic mini-projects

Hackathons

Portfolio projects

👨‍💻 Author
Aadhi
AI Developer | Data & Machine Learning Enthusiast

