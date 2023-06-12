import chardet
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns

with open('reviews.csv', 'rb') as f:
    result = chardet.detect(f.read())

# read the CSV file with the detected encoding
df = pd.read_csv('reviews.csv', encoding=result['encoding'])
grouped_df = df.groupby(['product_title','review_headline','review_date'])['cleaned_review'].apply(lambda x: ' '.join(x)).reset_index()
sentiment_df = pd.DataFrame(columns=['product_title', 'review_headline', 'review_date', 'Sentiment'])
# loop through each book and perform sentiment analysis on the concatenated reviews
for index, row in grouped_df.iterrows():
    review = row['cleaned_review']
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity

    # determine the sentiment label
    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
        # Add the sentiment analysis results to the new DataFrame
    sentiment_df.loc[index] = [row['product_title'], row['review_headline'], row['review_date'], sentiment_label]

    # Save the sentiment analysis results to a new CSV file
    sentiment_df.to_csv('sentiment_analysis_results.csv', index=False)


