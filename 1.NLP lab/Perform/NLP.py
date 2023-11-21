import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import os

# Define the input file path
input_file = 'sample.txt'

# Read the input text from the file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Task 3: Tokenize sentences and words
sentences = sent_tokenize(text)
words_in_sentences = [word_tokenize(sentence) for sentence in sentences]

# Task 4: Create a file containing word frequency
word_freq = Counter([word.lower() for sentence in words_in_sentences for word in sentence])
with open('output/word_frequency.txt', 'w', encoding='utf-8') as file:
    for word, freq in word_freq.items():
        file.write(f'{word}: {freq}\n')

# Task 5: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for sentence in words_in_sentences for word in sentence if word.lower() not in stop_words]

# Task 6: Create a vocabulary file
unique_words = set(filtered_words)
with open('output/vocabulary.txt', 'w', encoding='utf-8') as file:
    for word in unique_words:
        file.write(f'{word}\n')

# Task 7: Create index-to-word and word-to-index files
index_to_word = {i: word for i, word in enumerate(unique_words)}
word_to_index = {word: i for i, word in enumerate(unique_words)}

with open('output/index_to_word.txt', 'w', encoding='utf-8') as file:
    for index, word in index_to_word.items():
        file.write(f'{index}: {word}\n')

with open('output/word_to_index.txt', 'w', encoding='utf-8') as file:
    for word, index in word_to_index.items():
        file.write(f'{word}: {index}\n')

print("Tasks completed successfully!")
