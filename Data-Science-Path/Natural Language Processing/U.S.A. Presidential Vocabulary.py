# U.S.A. Presidential Vocabulary
#
# Whenever a United States of America president is elected or re-elected, an inauguration ceremony takes place to mark the beginning of the president’s term. 
# During the ceremony, the president gives an inaugural address to the nation, dictating the tone and focus of the next four years of leadership.
# In this project you will have the chance to analyze the inaugural addresses of the presidents of the United States of America, as collected by the Natural Language Toolkit, using word embeddings.
# By training sets of word embeddings on subsets of inaugural address versus the collection of presidents as a whole, we can learn about the different ways in which the presidents use language to convey their agenda.

import os
import gensim
import spacy
from president_helper import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

# get list of all speech files
files = sorted([file for file in os.listdir() if file[-4:] == '.txt'])
print(files)

# read each speech file
def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text

speeches= [read_file(file) for file in files]

# preprocess each speech
def process_speeches(speeches):
  word_tokenized_speeches = list()
  for speech in speeches:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
      word_tokenized_sentences.append(word_tokenized_sentence)
    word_tokenized_speeches.append(word_tokenized_sentences)
  return word_tokenized_speeches

processed_speeches = process_speeches(speeches)


# merge speeches
def merge_speeches(speeches):
  all_sentences = list()
  for speech in speeches:
    for sentence in speech:
      all_sentences.append(sentence)
  return all_sentences

all_sentences = merge_speeches(processed_speeches)

# view most frequently used words

def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()

most_freq_words = most_frequent_words(all_sentences)


# create gensim model of all speeches
all_prez_embeddings = gensim.models.Word2Vec(all_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom
similar_to_freedom = all_prez_embeddings.most_similar('freedom', topn=20)


# get President Roosevelt sentences
def get_president_sentences(president):
  files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
  speeches = [read_file(file) for file in files]
  processed_speeches = process_speeches(speeches)
  all_sentences = merge_speeches(processed_speeches)
  return all_sentences

roosevelt_sentences = get_president_sentences("franklin-d-roosevelt")


# view most frequently used words of Roosevelt
def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()

roosevelt_most_freq_words = most_frequent_words(roosevelt_sentences)


# create gensim model for Roosevelt
roosevelt_embeddings = gensim.models.Word2Vec(roosevelt_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for Roosevelt
roosevelt_similar_to_freedom = roosevelt_embeddings.most_similar('freedom', topn=20)


# get sentences of multiple presidents
def get_presidents_sentences(presidents):
  all_sentences = list()
  for president in presidents:
    files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
    speeches = [read_file(file) for file in files]
    processed_speeches = process_speeches(speeches)
    all_prez_sentences = merge_speeches(processed_speeches)
    all_sentences.extend(all_prez_sentences)
  return all_sentences

rushmore_prez_sentences = get_presidents_sentences(["washington","jefferson","lincoln","theodore-roosevelt"])

# view most frequently used words of presidents
rushmore_most_freq_words = most_frequent_words(rushmore_prez_sentences)
print(rushmore_most_freq_words)

# create gensim model for the presidents
rushmore_embeddings = gensim.models.Word2Vec(rushmore_prez_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for presidents
rushmore_similar_to_freedom = roosevelt_embeddings.most_similar('freedom', topn=20)
