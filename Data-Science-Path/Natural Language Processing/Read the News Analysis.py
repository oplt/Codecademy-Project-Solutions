# Read the News Analysis

# Given the vast amount of news articles in circulation, identifying and organizing articles by topic is a useful activity. 
# This can help you sift through the enormous amount of information out there so you can find the news relevant to your interests, or even allow you to build a news recommendation engine!
# The News International is the largest English language newspaper in Pakistan, covering local and international news across a variety of sectors. 
# A selection of articles from a Kaggle Dataset of The News International articles is provided in the workspace.
# In this project you will use term frequency-inverse document frequency (tf-idf) to analyze each article’s content and uncover the terms that best describe each article, providing quick insight into each article’s topic.

import codecademylib3_seaborn
import pandas as pd
import numpy as np
from articles import articles
from preprocessing import preprocess_text
import nltk, re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

# import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

# view article
print(articles[5])

# preprocess articles
stop_words = stopwords.words('english')
normalizer = WordNetLemmatizer()

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

def preprocess_text(text):
  cleaned = re.sub(r'\W+', ' ', text).lower()
  tokenized = word_tokenize(cleaned)
  normalized = " ".join([normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized if not re.match(r'\d+',token)])
  return normalized
processed_articles = [preprocess_text(article) for article in articles]

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()

# convert counts to tf-idf
word_counts = vectorizer.fit_transform(processed_articles)

# initialize and fit TfidfVectorizer
transformer = TfidfTransformer(norm=None)
tfidf_scores = transformer.fit_transform(word_counts)
vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_articles)
tfidf_scores_transformed = transformer.fit_transform(word_counts)
# check if tf-idf scores are equal
if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
  print(pd.DataFrame({'Are the tf-idf scores the same?':['YES']}))
else:
  print(pd.DataFrame({'Are the tf-idf scores the same?':['No, something is wrong :(']}))

# get vocabulary of terms
try:
  feature_names = vectorizer.get_feature_names()
except:
  pass

# get article index
try:
  article_index = [f"Article {i+1}" for i in range(len(articles))]
except:
  pass

# create pandas DataFrame with word counts
try:
  df_word_counts = pd.DataFrame(counts.T.todense(), index=feature_names, columns=article_index)
  print(df_word_counts)
except:
  pass

# create pandas DataFrame(s) with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores_transformed.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)
  print(df_tf_idf)
except:
  pass

# get highest scoring tf-idf term for each article
for i in range(1, 10):
  print(df_tf_idf[[f'Article {i}']].idxmax())
