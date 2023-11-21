import nltk
nltk.download('punkt')

# 3. Tokenize sentences.


print('\n*************************************************')
print("Sentences Tokenization")
from nltk.tokenize import sent_tokenize
text = """The voice that navigated was definitely that of a machine, and yet you could tell that the machine was a woman, which hurt my mind a little. How can machines have genders? The machine also had an American accent. How can machines have nationalities? This can't be a good idea, making machines talk like real people, can it? Giving machines humanoid identities?"""
text_to_sentence = sent_tokenize(text)
print(text_to_sentence)


# 3. Tokenize words in every sentence.

print('\n*************************************************')
print("Word Tokenization")
from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word) 
print() 

# 4. Create file containing words and their frequency of occurrence in document.

print('\n*************************************************')
print("Frequency Distribution of words")
from nltk.probability import FreqDist
freq_dist_of_words = FreqDist(tokenized_word)
print(freq_dist_of_words)

print(freq_dist_of_words.most_common())


# 5. Remove stopwords.
print('\n*************************************************')
print("Remove stopwords")
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
# print(stop_words)

text = 'Learn to lose your destiny to find where it leads you'
filtered_text = []
tokenized_word = word_tokenize(text)
for each_word in tokenized_word:
    if each_word not in stop_words:
        filtered_text.append(each_word)
print('Toxenized list with stop words: {}'.format(tokenized_word))
print('Toxenized list with out stop words: {}'.format(filtered_text))
print()

# 6. Create vocabulary (unique words. one word per line) for remaining words after removal of stopwords and store a file



# 7. Create index-to-word and word-to-index files to establish connection between word and its probable index to access it later.
