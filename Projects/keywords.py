import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import math

def generate_keywords(text, num_keywords=5):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Perform lemmatization
    lemmatizer = WordNetLemmatizer()
    filtered_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    # Count word frequencies
    word_freq = Counter(filtered_tokens)

    # Select top keywords
    top_keywords = word_freq.most_common(num_keywords)

    return [keyword[0] for keyword in top_keywords]

# Example usage
with open("text.txt", "r") as file:
    a = file.read()

text_length = len(a)
num_keywords = math.isqrt(text_length)  # Calculate the square root of text length

keywords = generate_keywords(a, num_keywords)
print("Keywords:", keywords)