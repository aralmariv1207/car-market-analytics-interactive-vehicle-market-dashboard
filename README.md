# Car Market Analytics: Interactive Vehicle Market Dashboard

## About

An interactive Streamlit web application for analyzing US vehicle market trends, featuring dynamic Plotly visualizations and real-time data filtering.

> **🚀 [View the Live Interactive Dashboard here](https://vehicle-market-interactive-dashboard.streamlit.app/)**


## 🚀 Technical Highlights

* **Interactive Data Visualization:** Developed a dynamic web dashboard using **Streamlit** and **Plotly Express**, allowing users to explore vehicle market trends through customizable charts.
* **Exploratory Data Analysis (EDA):** Performed comprehensive analysis on a 50k+ vehicle dataset, identifying key correlations between price, mileage, and vehicle condition.
* **User-Centric Features:** Implemented interactive widgets, including checkboxes and histograms, to allow real-time filtering of data distributions (e.g., odometer readings vs. price).
* **Production-Ready Code:** Structured the application with clear modular logic, ensuring high performance and scalability for cloud deployment.

---

## 📂 Data Information
The application utilizes the `vehicles_us.csv` dataset, containing over 50,000 records of vehicle listings. For repository efficiency, the raw data is stored in the `/data` directory, while the application logic in `app.py` leverages Streamlit's `@st.cache_data` for optimized performance.
