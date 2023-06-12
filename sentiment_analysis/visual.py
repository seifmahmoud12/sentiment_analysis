import chardet
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns


with open('sentiment_analysis_results.csv', 'rb') as f:
    result = chardet.detect(f.read())

# read the CSV file with the detected encoding
df = pd.read_csv('sentiment_analysis_results.csv', encoding=result['encoding'])

# sentiment_counts = df.groupby(['product_title', 'review_date', 'Sentiment']).size().unstack(fill_value=0).reset_index()
#
# # create a stacked bar chart of sentiment counts by product and date
# sentiment_counts.plot(x='review_date', kind='bar', stacked=True)
# plt.title('Sentiment Analysis by ProductTitle and Date')
# plt.xlabel('Date')
# plt.ylabel('Sentiment Count')
# plt.legend(title='Sentiment', loc='upper right')
# plt.show()
# from wordcloud import WordCloud
#
# text = ' '.join(df['cleaned_review'])
# wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
# plt.figure(figsize=(8, 8))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


# sns.histplot(df['Sentiment'], bins=10)
# plt.title('Histogram of Sentiment Scores')
# plt.xlabel('Sentiment Score')
# plt.ylabel('Number of Reviews')
# plt.show()

#
# sentiment_counts =df['Sentiment'].value_counts()
# plt.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%')
# plt.title('Sentiment Distribution of Book Reviews')
# plt.show()
# from wordcloud import WordCloud
#
# text = ' '.join(df['review_headline'])
# wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
# plt.figure(figsize=(8, 8))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()
