import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import re

# --- 1. HELPER FUNCTION ---
def clean_col_names(df):
    cols = df.columns
    new_cols = []
    for col in cols:
        name = re.sub(r'[\(\)\[\]\{\}\n]', '', str(col))
        name = re.sub(r'\s+', ' ', name)
        name = name.strip()
        new_cols.append(name)
    df.columns = new_cols
    return df

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    historical_data = pd.read_csv('cleaned_model_ready_data.csv', index_col='date', parse_dates=True)
    forecast_data = pd.read_csv('3_month_forecast_all_kpis.csv', index_col=0, parse_dates=True)
    forecast_data.index.name = 'date'
    correlation_data = pd.read_csv('cleaned_correlation_matrix.csv', index_col=0)
    
    historical_data = clean_col_names(historical_data)
    forecast_data = clean_col_names(forecast_data)
    correlation_data = clean_col_names(correlation_data)
    correlation_data.index = correlation_data.columns
    
    return historical_data, forecast_data, correlation_data

# --- Load the data ---
historical_df, forecast_df, correlation_df = load_data()
original_forecast = forecast_df.copy()

# --- 3. APP LAYOUT ---
st.title("🚗 Dealership Sales & KPI Forecasting Dashboard")

# --- Sidebar Controls ---
st.sidebar.header("Interactive Controls")
st.sidebar.markdown("Create a 'what-if' scenario by adjusting a KPI.")

kpi_to_adjust = st.sidebar.selectbox(
    "1. Select KPI to Adjust",
    options=forecast_df.columns
)

percentage_change = st.sidebar.slider(
    "2. Set Percentage Change (%)",
    min_value=-50, max_value=50, value=0, step=5
)

# --- 4. "WHAT-IF" SCENARIO LOGIC ---
adjusted_forecast = original_forecast.copy()
if percentage_change != 0:
    change_factor = 1 + (percentage_change / 100)
    original_value = adjusted_forecast[kpi_to_adjust]
    change_amount = original_value * (change_factor - 1)
    adjusted_forecast[kpi_to_adjust] = original_value * change_factor
    for kpi in adjusted_forecast.columns:
        if kpi != kpi_to_adjust:
            correlation_value = correlation_df.loc[kpi_to_adjust, kpi]
            correlated_change = change_amount * correlation_value
            adjusted_forecast[kpi] += correlated_change

# --- 5. VISUALIZATION OF MAIN KPI ---
st.sidebar.markdown("---")
st.sidebar.header("Chart Display")

selected_kpi_display = st.sidebar.selectbox(
    "Select a KPI to Visualize",
    options=historical_df.columns,
    index=list(historical_df.columns).index(kpi_to_adjust)
)

st.header(f"Results for: {selected_kpi_display}")

# Prepare data for plotting
plot_df_hist = historical_df[selected_kpi_display]
last_hist_point = plot_df_hist.tail(1)
plot_df_adj = adjusted_forecast[selected_kpi_display]
continuous_forecast_df = pd.concat([last_hist_point, plot_df_adj])

# Create an empty figure object
fig = go.Figure()
fig.add_trace(go.Scatter(x=plot_df_hist.index, y=plot_df_hist, mode='lines', name='Historical', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=continuous_forecast_df.index, y=continuous_forecast_df, mode='lines', name='Forecast (Adjusted)', line=dict(color='red')))
fig.add_vline(x=historical_df.index.max(), line_dash="dash", line_color="grey")

# Update layout for better date display
fig.update_layout(
    title=f'"{selected_kpi_display}" Over Time',
    xaxis_title="Date",
    yaxis_title="Monthly Value",
    xaxis=dict(tickformat='%b\n%Y') # Format: "Jan\n2024"
)

st.plotly_chart(fig, use_container_width=True)

# --- 6. VISUALIZATION OF RELATED KPIS (Full 3-Month View) ---
st.header("Impact on Top 10 Related KPIs") # Changed header from 5 to 10
if percentage_change != 0:
    st.write(f"Because you adjusted **{kpi_to_adjust}** by **{percentage_change}%**, the forecasts for the most related KPIs have also changed.")
    
    # --- THIS IS THE LINE THAT WAS CHANGED ---
    # Find the top 10 most related KPIs
    correlations = correlation_df[kpi_to_adjust].drop(kpi_to_adjust)
    top_10_related_kpis = correlations.abs().nlargest(10) # Changed 5 to 10
    
    # Get the original and adjusted forecasts for these KPIs
    original_slice = original_forecast[top_10_related_kpis.index].T
    adjusted_slice = adjusted_forecast[top_10_related_kpis.index].T
    
    # Rename columns for clarity
    original_slice.columns = ['Original (Jan)', 'Original (Feb)', 'Original (Mar)']
    adjusted_slice.columns = ['Adjusted (Jan)', 'Adjusted (Feb)', 'Adjusted (Mar)']
    
    # Combine into a single summary table
    summary_df = pd.concat([original_slice, adjusted_slice], axis=1)
    
    # Reorder columns for better comparison
    summary_df = summary_df[['Original (Jan)', 'Adjusted (Jan)', 'Original (Feb)', 'Adjusted (Feb)', 'Original (Mar)', 'Adjusted (Mar)']]
    
    # Format the table for better display
    st.dataframe(summary_df.style.format('{:,.2f}'))
else:
    st.write("Move the slider in the sidebar to see the impact on other KPIs.")