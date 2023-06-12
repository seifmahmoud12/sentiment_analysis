import chardet
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

import re

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


with open('amazonproj.csv', 'rb') as f:
    result = chardet.detect(f.read())

df = pd.read_csv('amazonproj.csv', encoding=result['encoding'])
lemmatizer= WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# define a function to preprocess each review
def preprocess_review(review):
    #special character removers
    review = re.sub(r'[^a-zA-Z0-9\s]', '', review)

    # convert the review to lowercase
    review = review.lower()
    # tokenize the review into words
    words = word_tokenize(review)
    # remove stopwords from the review
    words = [word for word in words if word not in stop_words]
    # lemmatize the words in the review
    words = [lemmatizer.lemmatize(word) for word in words]
    # join the words back into a string

    cleaned_review = ' '.join(words)

    return cleaned_review

df['cleaned_review'] = df['review_body'].apply(preprocess_review)
df.to_csv('reviews.csv', index=False)