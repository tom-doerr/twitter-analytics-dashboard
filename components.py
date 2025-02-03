import streamlit as st
import pandas as pd

def render_metrics_section(stats):
    """Render the metrics section with key statistics."""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Posts", f"{stats['Total Posts']:,}")
        st.metric("Total Likes", f"{stats['Total Likes']:,}")
    
    with col2:
        st.metric("Total Impressions", f"{stats['Total Impressions']:,}")
        st.metric("Total Reposts", f"{stats['Total Reposts']:,}")
    
    with col3:
        st.metric("Avg Engagement", f"{stats['Average Engagement']:.2f}")
        st.metric("Date Range", stats['Date Range'])

def render_data_explorer(df):
    """Render the data explorer section with filters and table."""
    st.subheader("Data Explorer")
    
    # Add search filter
    search_term = st.text_input("Search in Post Text", "")
    
    # Date range filter
    date_range = st.date_input(
        "Select Date Range",
        [df['Date'].min(), df['Date'].max()],
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Filter data
    filtered_df = df.copy()
    if search_term:
        filtered_df = filtered_df[filtered_df['Post text'].str.contains(search_term, case=False, na=False)]
    
    filtered_df = filtered_df[
        (filtered_df['Date'].dt.date >= date_range[0]) &
        (filtered_df['Date'].dt.date <= date_range[1])
    ]
    
    # Display filtered dataframe
    st.dataframe(
        filtered_df[['Date', 'Post text', 'Impressions', 'Likes', 'Total_Engagement']],
        height=400
    )

def render_top_posts(df):
    """Render the top posts section."""
    st.subheader("Top Performing Posts")
    
    metric = st.selectbox(
        "Select Metric",
        ['Total_Engagement', 'Likes', 'Impressions', 'Reposts']
    )
    
    top_posts = df.nlargest(5, metric)[['Date', 'Post text', metric]]
    
    for _, post in top_posts.iterrows():
        with st.container():
            st.markdown(f"**{post['Date'].strftime('%Y-%m-%d')}** ({post[metric]:,} {metric})")
            st.markdown(post['Post text'])
            st.divider()
