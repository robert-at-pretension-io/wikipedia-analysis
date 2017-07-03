# will this ever be used... the world will never know
import tensorflow as tf

# scrape wiki plaintext
import wikipedia

# to view word freq dist
import matplotlib.pyplot
import tkinter

# store the articles so we don't annoy wikipedia (TODO)
# (might change to database storage later)
import _pickle as cPickle


# commonly used words...
import re
import os.path
import urllib.request

from stop_words import get_stop_words
import nltk

from nltk.corpus import stopwords


nltk.download("stopwords")
nltk.download("punkt")

test = stopwords.words('english')

common_words = get_stop_words(language='english', cache=True)

fn = '10k_common.txt'

if os.path.isfile(fn):
    print("already downloaded the common words list")
    myfile = open(fn, 'r')
    most_common = [line for line in myfile.readlines()]
else:
    print('ayyyy lemme download that common word list file for you!')
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt'
    urllib.request.urlretrieve(url, filename=fn)
    myfile = open(fn, 'r')
    most_common = [line for line in myfile.readlines()]


concat_list = list(set(s.lower().strip() for s in test + common_words + most_common))

# print(concat_list, sep='\n')


# get wiki page
math = wikipedia.page(title='wavelength',  auto_suggest=True, redirect=True, preload=False)

# print(math.content)

tokens = nltk.word_tokenize(math.content)

must_contain_some_letters = re.compile("[a-zA-Z]+")

words = [w.lower() for w in tokens]

# remove symbols and numbers only
words = list(filter(must_contain_some_letters.match, words))

# remove stop words
words = [w for w in words if w not in concat_list]

fd = nltk.FreqDist(words)

# sorts the most frequent words
top_10_best_words_omg = []
for w in set(words):
    top_10_best_words_omg.append((w, words.count(w)))

top_10_best_words_omg.sort(key=lambda x: x[1], reverse=True)
# sort by the second element in the tuple

# fd.plot(50, cumulative=False)
