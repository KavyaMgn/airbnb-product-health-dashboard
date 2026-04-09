import pandas as pd

# Load
reviews = pd.read_csv('reviews.csv')
listings = pd.read_csv('listings.csv')

# --- Clean Reviews ---
reviews['date'] = pd.to_datetime(reviews['date'])
reviews = reviews.dropna(subset=['comments'])
reviews = reviews[reviews['date'] >= '2022-01-01']  # last 3 years = most relevant

# --- Clean Listings ---
_price = listings['price']
if _price.dtype == object:
    _price = _price.replace(r'[\$,]', '', regex=True)
listings['price'] = pd.to_numeric(_price, errors='coerce')
# Only drop $0 listings when price is present; keep rows if price is missing for whole scrape
if listings['price'].notna().any():
    listings = listings[listings['price'].isna() | (listings['price'] > 0)]
listings = listings.dropna(subset=['review_scores_rating'])

# --- Save cleaned files ---
reviews.to_csv('reviews_clean.csv', index=False)
listings.to_csv('listings_clean.csv', index=False)

# --- Sanity check ---
print("✅ Reviews:", reviews.shape)
print("   Date range:", reviews['date'].min(), "to", reviews['date'].max())
print("\n✅ Listings:", listings.shape)
if listings['price'].notna().any():
    print("   Price range: $", listings['price'].min(), "to $", listings['price'].max())
else:
    print("   Price: (all missing in this dataset)")
avg_rating = listings['review_scores_rating'].mean()
print(
    "   Avg rating:",
    round(avg_rating, 2) if pd.notna(avg_rating) else "n/a",
)
