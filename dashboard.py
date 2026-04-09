import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
reviews = pd.read_csv('reviews_sentiment.csv')
listings = pd.read_csv('listings_clean.csv')

reviews['date'] = pd.to_datetime(reviews['date'])
reviews['month'] = reviews['date'].dt.to_period('M').astype(str)

st.set_page_config(page_title="Airbnb NYC Product Health", layout="wide")
st.title("🏠 Airbnb NYC — Product Health Dashboard")
st.caption("Analyzing 50,000 guest reviews | Data: Inside Airbnb")

# --- Row 1: KPI Cards ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews Analyzed", "50,000")
col2.metric("Positive Sentiment", f"{round(42379/50000*100, 1)}%")
col3.metric("Negative Sentiment", f"{round(424/50000*100, 1)}%")
col4.metric("Avg Sentiment Score", "0.382")

st.divider()

# --- Row 2: Sentiment Over Time ---
st.subheader("📈 Sentiment Trend Over Time")
monthly = reviews.groupby(['month', 'sentiment_label']).size().reset_index(name='count')
fig1 = px.line(
    monthly[monthly['sentiment_label'] == 'Positive'],
    x='month', y='count',
    title='Positive Reviews Per Month',
    color_discrete_sequence=['#FF5A5F']
)
st.plotly_chart(fig1, use_container_width=True)

# --- Row 3: Sentiment Distribution ---
st.subheader("🥧 Sentiment Breakdown")
col1, col2 = st.columns(2)

dist = reviews['sentiment_label'].value_counts().reset_index()
dist.columns = ['Sentiment', 'Count']
fig2 = px.pie(dist, names='Sentiment', values='Count',
              color_discrete_sequence=['#FF5A5F', '#767676', '#00A699'])
col1.plotly_chart(fig2, use_container_width=True)

# --- Row 4: Neighborhood Ratings ---
st.subheader("📍 Top Neighborhoods by Rating")
top_hoods = listings.groupby('neighbourhood_cleansed')['review_scores_rating'].mean().sort_values(ascending=False).head(15).reset_index()
top_hoods.columns = ['Neighborhood', 'Avg Rating']
fig3 = px.bar(top_hoods, x='Avg Rating', y='Neighborhood',
              orientation='h', color='Avg Rating',
              color_continuous_scale='RdYlGn')
col2.plotly_chart(fig3, use_container_width=True)

# --- Row 5: Sample Negative Reviews ---
st.subheader("🔍 What Are Guests Complaining About?")
negatives = reviews[reviews['sentiment_label'] == 'Negative'][['date', 'comments']].sample(10, random_state=42)
st.dataframe(negatives, use_container_width=True)
