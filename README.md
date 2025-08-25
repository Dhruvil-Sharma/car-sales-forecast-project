# Interactive Sales & KPI Forecasting Dashboard

This project delivers a comprehensive forecasting dashboard designed to help a car dealership with strategic planning and decision-making. The application uses historical sales data to predict future KPIs, analyzes the relationships between different business metrics, and provides an interactive tool to simulate "what-if" scenarios.

---

### 🚀 Live Demo

[**Insert a GIF of your running Streamlit application here. This is highly recommended!**]

*(To create a GIF, you can use a free tool like ScreenToGif or Giphy Capture to record your screen while you use the dashboard's features.)*

---

### ✨ Key Features

-   **3-Month KPI Forecasting:** Utilizes a SARIMAX time-series model to predict all business KPIs for the next three months.
-   **Interactive "What-If" Scenarios:** A key feature of the dashboard is a control panel that allows users to adjust the forecast for any single KPI (e.g., increase new car sales by 15%).
-   **Automatic Impact Analysis:** When a "what-if" scenario is created, the dashboard instantly calculates and displays the ripple effect on the Top 10 most correlated KPIs, showing the full impact of a business decision.
-   **Dynamic Visualizations:** The dashboard features a clean, interactive chart built with Plotly to explore both historical data and the adjusted forecasts.

---

### 🛠️ How to Run

1.  **Clone the repository or download the project files.**
2.  **Install the required libraries from your terminal:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit application from your terminal:**
    ```bash
    streamlit run app.py
    ```
    The interactive dashboard will open in your web browser.

---

### 🔬 Data Analysis & Modeling

The project followed a structured data science workflow, detailed in the `project_main.ipynb` notebook:

1.  **Data Cleaning:** The raw data was extensively cleaned by imputing missing values, standardizing hundreds of KPI names to merge duplicates, and removing low-information (all-zero) columns.
2.  **Forecasting Model:** A SARIMAX model was chosen for its ability to handle the strong seasonality present in the sales data. A separate model was trained for each KPI.

---

### 📂 File Descriptions

| File Name | Description |
| :--- | :--- |
| **`app.py`** | The Python script for the final, interactive Streamlit dashboard. |
| **`project_main.ipynb`** | The Jupyter Notebook containing the end-to-end data analysis and model development. |
| **`requirements.txt`** | A list of the necessary Python libraries to run the project. |
| **`FS-data-80475.csv`** | The original, raw historical dataset (2022-2024). |
| **`cleaned_model_ready_data.csv`**| The final, cleaned, and pivoted dataset used for model training. |
| **`3_month_forecast_all_kpis.csv`** | The output of the forecasting model, containing the 3-month forecast for 2025. |
| **`cleaned_correlation_matrix.csv`** | The calculated correlation matrix, used by the Streamlit app for the what-if scenarios. |

---

### 💻 Technologies Used

-   Python
-   Pandas
-   Statsmodels (SARIMAX)
-   Streamlit
-   Plotly
