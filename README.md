# 🏠 Airbnb NYC — Product Health Dashboard

🚀 **[View Live Dashboard](https://airbnb-appuct-health-dashboard-bjfjvcpuf4kvei38c3ozan.streamlit.app)**

A product analytics project analyzing 562,000+ guest reviews to assess 
the health of Airbnb's NYC marketplace and surface actionable insights 
for the product team.

---

## 🔍 What This Project Does

- Cleans and processes 562,313 Airbnb NYC guest reviews (2022–2026)
- Runs sentiment analysis on 50,000 sampled reviews using TextBlob
- Visualizes sentiment trends, neighborhood ratings, and guest complaints
- Delivers a PM-style memo with findings and recommendations

---

## 📊 Key Findings

- **84.8%** of reviews are positive — overall guest satisfaction is high
- **Listing misrepresentation** is the #1 driver of negative reviews
- **Sentiment dipped in 2024** coinciding with NYC's Local Law 18 regulations
- **Outer borough neighborhoods** (Belle Harbor, Breezy Point) outperform 
  Manhattan on avg ratings

---

## 🛠️ Tech Stack

- **Python** — pandas, TextBlob, Plotly
- **Streamlit** — interactive dashboard
- **Data Source** — [Inside Airbnb](https://insideairbnb.com/new-york-city/)

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas textblob plotly streamlit

# Run data pipeline
python3 clean.py
python3 sentiment.py

# Launch dashboard
streamlit run dashboard.py
```

---

## 📁 Project Structure
├── explore_data.py      # Initial data exploration
├── clean.py             # Data cleaning pipeline
├── sentiment.py         # Sentiment analysis
├── dashboard.py         # Streamlit dashboard
├── PM_MEMO.md           # Product analyst memo with recommendations

---

## 📄 PM Memo
See [PM_MEMO.md](PM_MEMO.md) for full findings and recommendations.
