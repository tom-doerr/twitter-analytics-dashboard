import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def load_and_process_data(file_path):
    """Load and process the Twitter analytics data."""
    # Handle both string paths and uploaded file objects
    if isinstance(file_path, str):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_csv(file_path)

    # Convert date string to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Calculate total engagement
    engagement_columns = ['Likes', 'Engagements', 'Bookmarks', 'Share', 
                         'Replies', 'Reposts', 'Profile visits', 'Detail expands']
    df['Total_Engagement'] = df[engagement_columns].sum(axis=1)

    return df

def create_time_series_plot(df, metric):
    """Create a time series plot for the specified metric."""
    daily_data = df.groupby('Date')[metric].sum().reset_index()

    fig = px.line(daily_data, x='Date', y=metric,
                  title=f'{metric} Over Time',
                  template='plotly_white')

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=metric,
        hovermode='x unified'
    )

    return fig

def create_engagement_distribution(df):
    """Create a box plot of engagement metrics."""
    metrics = ['Likes', 'Bookmarks', 'Share', 'Replies', 'Reposts']
    data = []

    for metric in metrics:
        data.append(go.Box(y=df[metric], name=metric))

    fig = go.Figure(data=data)
    fig.update_layout(
        title='Engagement Metrics Distribution',
        yaxis_title='Count',
        template='plotly_white',
        showlegend=False
    )

    return fig

def get_top_posts(df, metric, n=5):
    """Get top performing posts based on specified metric."""
    return df.nlargest(n, metric)[['Date', 'Post text', metric]]

def calculate_summary_stats(df):
    """Calculate summary statistics for the dataset."""
    stats = {
        'Total Posts': len(df),
        'Total Impressions': df['Impressions'].sum(),
        'Total Likes': df['Likes'].sum(),
        'Total Reposts': df['Reposts'].sum(),
        'Average Engagement': df['Total_Engagement'].mean(),
        'Date Range': f"{df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}"
    }
    return stats