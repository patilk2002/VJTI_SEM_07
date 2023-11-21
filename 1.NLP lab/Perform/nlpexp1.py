# Import necessary libraries
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import os

# Define the input file path (replace 'your_input_file.txt' with your file path)
input_file = 'sample.txt'

# Read the input text from the file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Task 3: Tokenize sentences and words
sentences = sent_tokenize(text)  # Tokenize the text into sentences
words_in_sentences = [word_tokenize(sentence) for sentence in sentences]  # Tokenize each sentence into words

# Task 4: Create a file containing word frequency
word_freq = Counter([word.lower() for sentence in words_in_sentences for word in sentence])  # Count word frequency
with open('output/word_frequency.txt', 'w', encoding='utf-8') as file:
    for word, freq in word_freq.items():
        file.write(f'{word}: {freq}\n')  # Write word and its frequency to the file

# Task 5: Remove stopwords
stop_words = set(stopwords.words('english'))  # Get a set of English stopwords
filtered_words = [word for sentence in words_in_sentences for word in sentence if word.lower() not in stop_words]

# Task 6: Create a vocabulary file
unique_words = set(filtered_words)  # Get unique words after removing stopwords
with open('output/vocabulary.txt', 'w', encoding='utf-8') as file:
    for word in unique_words:
        file.write(f'{word}\n')  # Write each unique word to the vocabulary file

# Task 7: Create index-to-word and word-to-index files
index_to_word = {i: word for i, word in enumerate(unique_words)}  # Create a mapping from index to word
word_to_index = {word: i for i, word in enumerate(unique_words)}  # Create a mapping from word to index

with open('output/index_to_word.txt', 'w', encoding='utf-8') as file:
    for index, word in index_to_word.items():
        file.write(f'{index}: {word}\n')  # Write index-to-word mapping to a file

with open('output/word_to_index.txt', 'w', encoding='utf-8') as file:
    for word, index in word_to_index.items():
        file.write(f'{word}: {index}\n')  # Write word-to-index mapping to a file

print("Tasks completed successfully!")  # Print a message to indicate successful completion
