import pandas as pd
from textblob import TextBlob

# Load cleaned reviews
reviews = pd.read_csv('reviews_clean.csv')

# Sample 50k reviews for speed (1M takes too long)
reviews = reviews.sample(50000, random_state=42)

# Score each comment — polarity is -1 (negative) to +1 (positive)
def get_sentiment(text):
    try:
        return TextBlob(str(text)).sentiment.polarity
    except Exception:
        return 0

print("Running sentiment analysis... (takes ~1-2 mins)")
reviews['sentiment_score'] = reviews['comments'].apply(get_sentiment)

# Label as Positive, Neutral, Negative
def label(score):
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

reviews['sentiment_label'] = reviews['sentiment_score'].apply(label)

# Save
reviews.to_csv('reviews_sentiment.csv', index=False)

# Summary
print("\n✅ Sentiment Distribution:")
print(reviews['sentiment_label'].value_counts())
print("\nAvg sentiment score:", round(reviews['sentiment_score'].mean(), 3))
