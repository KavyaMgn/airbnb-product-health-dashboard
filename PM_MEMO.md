# 🏠 Airbnb NYC — Product Health Analysis
**Analyst:** Kavya Murugan  
**Date:** April 2026  
**Data Source:** Inside Airbnb (50,000 guest reviews, 24,949 listings)

---

## Executive Summary
Guest sentiment on Airbnb NYC is overwhelmingly positive (84.8%), 
but a concentrated set of negative reviews reveal 3 fixable product 
problems that likely drive churn and erode trust.

---

## What I Found

### 1. Listing Misrepresentation is the #1 complaint
Guests repeatedly flag that listings don't match reality —
luxury labels on basic apartments, shared spaces not clearly 
disclosed, misleading photos. This is a trust problem, not a 
host quality problem.

**Signal:** "Listed as a luxury condo. Clearly NOT a luxury condo."

### 2. Sentiment dipped in 2024 and hasn't recovered
The trend line shows a clear drop in positive review volume 
in early 2024, coinciding with NYC's Local Law 18 (short-term 
rental regulations) which reduced supply and likely pushed 
lower-quality listings to the top.

### 3. Outer borough neighborhoods outperform Manhattan on ratings
Belle Harbor, Breezy Point, and Castleton Corners have higher 
avg ratings than core Manhattan neighborhoods — suggesting 
quality supply exists outside tourist corridors but is 
undiscovered.

---

## Recommendations

| Priority | Recommendation | Expected Impact |
|---|---|---|
| P0 | Add verified listing badges for accuracy | Reduce misrepresentation complaints |
| P1 | Require hosts to disclose shared spaces at listing creation | Reduce surprise/negative reviews |
| P2 | Surface outer-borough gems in search ranking | Improve avg guest satisfaction |

---

## Metrics to Track Going Forward
- Monthly sentiment score (target: maintain >0.38)
- % of reviews mentioning "misleading" or "not as described"
- Rating distribution by neighborhood over time
- Negative review response rate by hosts

---

## Methodology
- 562,313 reviews cleaned (2022–2026)
- 50,000 sampled for sentiment analysis using TextBlob
- Sentiment scored: Positive >0.1, Negative <-0.1, Neutral in between
- Neighborhood ratings from 24,949 active listings
