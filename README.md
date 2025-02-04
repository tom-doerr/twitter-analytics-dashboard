# Twitter Analytics Dashboard

A Streamlit-based dashboard for visualizing and analyzing Twitter/X analytics data. This interactive dashboard provides insights into your Twitter engagement metrics, trends, and top-performing posts.

🔗 **[Live Demo](https://data-visualizer-tom-doerr.replit.app/)**

## Features

- 📊 Interactive metrics dashboard
- 📈 Engagement trend analysis
- 🔍 Data exploration with filtering capabilities
- 🏆 Top performing posts analysis
- 📁 Support for custom CSV file uploads

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/twitter-analytics-dashboard.git
cd twitter-analytics-dashboard
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Either use the default data or upload your own Twitter analytics CSV file through the interface

## Data Format

The dashboard expects a CSV file with the following columns:
- Post id
- Date
- Post text
- Impressions
- Likes
- Engagements
- Bookmarks
- Share
- Replies
- Reposts
- Profile visits
- Detail expands

## Dependencies

- Python 3.11+
- Streamlit
- Pandas
- Plotly

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

MIT License