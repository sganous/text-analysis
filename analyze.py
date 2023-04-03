import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from collections import Counter

# Download dependency
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Define a function to check if a word is a noun
def is_noun(tag):
    return tag.startswith('N')

# Input sentence
sentence = input("Enter a sentence: ")
# Tokenize the sentence into words
words = word_tokenize(sentence)
# Tag the words with parts of speech
tags = [tag for word, tag in nltk.pos_tag(words)]
# Count the number of nouns in the sentence
noun_count = sum([1 for tag in tags if is_noun(tag)])
# Calculate the average length of all words in the sentence
avg_word_length = round(sum([len(word) for word in words]) / len(words), 2)

# Output the results to a CSV file
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['noun_count', 'avg_word_length']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'noun_count': noun_count, 'avg_word_length': avg_word_length})
