# Car Dealership KPI Forecasting and Analysis Dashboard

## 1. Problem Statement

The goal of this project was to develop a system for a car dealership to predict future Key Performance Indicators (KPIs) for the next three months. The system needed to include a forecasting model, correlation analysis, and an interactive "what-if" scenario dashboard to help with budget planning and decision-making.

## 2. File Descriptions

This repository contains the following files and folders:

| File Name | Description |
| :--- | :--- |
| **`app.py`** | The Python script for the final, interactive Streamlit dashboard. |
| **`project_main.ipynb`** | A Jupyter Notebook containing the end-to-end data analysis, including data cleaning, model training, and accuracy evaluation. |
| **`requirements.txt`** | A list of the necessary Python libraries required to run the project. |
| **`FS-data-80475.csv`** | The original, raw historical dataset (2022-2024) provided for the task. This is the starting point for the analysis. |
| **`cleaned_model_ready_data.csv`**| The final, cleaned, and pivoted dataset. This is the direct input for training the forecasting models. |
| **`3_month_forecast_all_kpis.csv`** | The output of the forecasting model, containing the predicted values for Jan, Feb, and Mar 2025 for all KPIs. |
| **`cleaned_correlation_matrix.csv`** | The calculated correlation matrix. This file is used as the "engine" for the what-if scenario in the Streamlit app. |

## 3. How to Run the Application

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

## 4. Key Features

-   **Data Preparation:** The raw dataset was thoroughly cleaned, handling missing values by imputation, standardizing KPI names to merge duplicates, and removing low-information (all-zero) columns.
-   **Prediction:** A SARIMA time-series model was trained for each KPI to generate a 3-month forecast.
-   **Correlation & "What-If" Analysis:** The dashboard features an interactive tool where adjusting one KPI's forecast automatically updates the forecasts of related KPIs based on their historical correlation.
-   **Interactive Dashboard:** A web dashboard built with Streamlit allows users to visualize historical data and forecasts for any KPI and explore the "what-if" scenarios.

## 5. Model Accuracy

The model's performance was evaluated using a chronological train-test split (trained on 2022-2023 data, tested on 2024 data).

-   **Mean Absolute Percentage Error (MAPE):** The MAPE for the **Top 10 most significant KPIs** was calculated to be **[Your MAPE Value] %**. This provides a realistic measure of the model's performance on the KPIs that are most critical to the business.



## 6. Technologies Used

-   **Python**
-   **Pandas**
-   **Statsmodels** (for SARIMA forecasting)
-   **Streamlit** (for the web dashboard)
-   **Plotly** (for interactive charts)
