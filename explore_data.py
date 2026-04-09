import pandas as pd

# Load data
reviews = pd.read_csv('reviews.csv')
listings = pd.read_csv('listings.csv')

# Reviews overview
print("=== REVIEWS ===")
print("Shape:", reviews.shape)
print("Columns:", reviews.columns.tolist())
print("Date range:", reviews['date'].min(), "to", reviews['date'].max())
print(reviews.head(3))

# Listings overview
print("\n=== LISTINGS ===")
print("Shape:", listings.shape)
print("Columns:", listings.columns.tolist())
print(listings[['name', 'price', 'room_type', 'review_scores_rating']].head(3))
