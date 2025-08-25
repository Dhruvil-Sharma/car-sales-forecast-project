# Car Dealership KPI Forecasting and Analysis Dashboard

## 1. Problem Statement

The goal of this project was to develop a system for a car dealership to predict future Key Performance Indicators (KPIs) for the next three months. The system needed to include a forecasting model, correlation analysis, and an interactive "what-if" scenario dashboard to help with budget planning and decision-making.

## 2. How to Run the Application

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

## 3. Key Features

This project successfully meets all the specified requirements:

-   **Data Preparation:** The raw dataset was thoroughly cleaned, handling missing values by imputation, standardizing KPI names to merge duplicates, and removing low-information (all-zero) columns.
-   **Prediction:** A SARIMAX time-series model was trained for each KPI to generate a 3-month forecast for Jan, Feb, and Mar 2025.
-   **Correlation & "What-If" Analysis:** A correlation matrix was calculated to understand the relationships between KPIs. The dashboard features an interactive tool where adjusting one KPI's forecast automatically updates the forecasts of related KPIs based on these correlations.
-   **Interactive Dashboard:** A web dashboard built with Streamlit allows users to:
    -   Visualize the historical data and 3-month forecast for any KPI.
    -   Interactively test "what-if" scenarios using a simple slider.
    -   Instantly see the financial impact on the Top 10 most related KPIs.

## 4. Model Accuracy

The model's performance was evaluated using a chronological train-test split (trained on 2022-2023 data, tested on 2024 data), which is the standard practice for validating time-series models.

-   **Mean Absolute Percentage Error (MAPE):** The MAPE for the **Top 10 most significant KPIs** was calculated to be **[Your MAPE Value] %**. This provides a realistic measure of the model's performance on the KPIs that are most critical to the business.

*(Note: A direct accuracy test against the provided 2025 data was not possible, as the file (`FS-data-80475-2025-all-months.csv`) was found to contain data for 2024, not 2025.)*

## 5. Technologies Used

-   **Python**
-   **Pandas** (for data manipulation and analysis)
-   **Statsmodels** (for SARIMAX time-series forecasting)
-   **Streamlit** (for building the interactive web dashboard)
-   **Plotly** (for data visualizations)
-   **Jupyter Notebook** (for initial analysis and model development)