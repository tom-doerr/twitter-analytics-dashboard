import streamlit as st
import pandas as pd
from utils import (
    load_and_process_data,
    create_time_series_plot,
    create_engagement_distribution,
    calculate_summary_stats
)
from components import render_metrics_section, render_data_explorer, render_top_posts

# Page configuration
st.set_page_config(
    page_title="Twitter Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stMetric {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.title("📊 Twitter Analytics Dashboard")

# Load and cache data
@st.cache_data
def load_data():
    return load_and_process_data("attached_assets/account_analytics_content_2024-11-06_2025-02-04.csv")

# Load data
try:
    df = load_data()
    
    # Calculate summary statistics
    stats = calculate_summary_stats(df)
    
    # Render metrics section
    render_metrics_section(stats)
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📈 Trends", "🔍 Data Explorer", "🏆 Top Posts"])
    
    with tab1:
        # Time series analysis
        st.subheader("Engagement Trends")
        metric = st.selectbox(
            "Select Metric",
            ['Impressions', 'Likes', 'Total_Engagement', 'Reposts']
        )
        st.plotly_chart(create_time_series_plot(df, metric), use_container_width=True)
        
        # Engagement distribution
        st.subheader("Engagement Distribution")
        st.plotly_chart(create_engagement_distribution(df), use_container_width=True)
    
    with tab2:
        render_data_explorer(df)
    
    with tab3:
        render_top_posts(df)

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • Data refreshed daily")
