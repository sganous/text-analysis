import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from collections import Counter

# Download dependency
nltk.download('wordnet')
nltk.download('punkt')
# Define a function to check if a word is a noun
def is_noun(word):
    synsets = wordnet.synsets(word)
    for synset in synsets:
        if synset.pos() == 'n':
            return True
    return False

# Input sentence
sentence = input("Enter a sentence: ")
# Tokenize the sentence into words
words = word_tokenize(sentence)
# Filter out non-alphabetic characters and convert all words to lowercase
words = [word.lower() for word in words if word.isalpha()]
# Count the number of nouns in the sentence
noun_count = sum([1 for word in words if is_noun(word)])
# Calculate the average length of all words in the sentence
avg_word_length = round(sum([len(word) for word in words]) / len(words), 2)

# Output the results to a CSV file
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['noun_count', 'avg_word_length']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'noun_count': noun_count, 'avg_word_length': avg_word_length})
