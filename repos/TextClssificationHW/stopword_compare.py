import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

# Function to extract words, optionally removing stopwords
def extract_words(text, remove_stopwords=False):
    stop_words = set(stopwords.words("english")) if remove_stopwords else set()
    return [
        word.lower() for word in word_tokenize(text) if any(c.isalpha() for c in word) and word.lower() not in stop_words
    ]

# Function to load words from a file
def load_file(file_name, remove_stopwords=False):
    total_lines = 0
    words = []

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            words.extend(extract_words(line, remove_stopwords))
            total_lines += 1

    return words, total_lines

# Function to compute word frequency
def calculate_word_frequency(words_in_positive, words_in_negative):
    frequency = {}

    for word in words_in_positive:
        if word in frequency:
            frequency[word][0] += 1
        else:
            frequency[word] = [1, 0]

    for word in words_in_negative:
        if word in frequency:
            frequency[word][1] += 1
        else:
            frequency[word] = [0, 1]

    return frequency

# Function to compute word probability with Laplace smoothing
def calculate_word_probability(frequency, words_in_positive, words_in_negative):
    probability = {}

    for word in frequency:
        positive = (frequency[word][0] + 1) / (len(words_in_positive) + len(frequency))
        negative = (frequency[word][1] + 1) / (len(words_in_negative) + len(frequency))
        probability[word] = [positive, negative]

    return probability

# Naive Bayes classification function
def classify(text, positive_reviews, negative_reviews, probability, remove_stopwords=False):
    words = extract_words(text, remove_stopwords)

    total_reviews = positive_reviews + negative_reviews
    positive = positive_reviews / total_reviews
    negative = negative_reviews / total_reviews

    for word in words:
        if word in probability:
            positive *= probability[word][0]
            negative *= probability[word][1]

    summation = positive + negative
    return (positive / summation, negative / summation)

# Load datasets (with and without stopwords)
words_pos, pos_reviews = load_file("positive_reviews.txt", remove_stopwords=False)
words_neg, neg_reviews = load_file("negative_reviews.txt", remove_stopwords=False)

words_pos_ns, pos_reviews_ns = load_file("positive_reviews.txt", remove_stopwords=True)
words_neg_ns, neg_reviews_ns = load_file("negative_reviews.txt", remove_stopwords=True)

# Compute probabilities (with and without stopwords)
word_freq = calculate_word_frequency(words_pos, words_neg)
word_prob = calculate_word_probability(word_freq, words_pos, words_neg)

word_freq_ns = calculate_word_frequency(words_pos_ns, words_neg_ns)
word_prob_ns = calculate_word_probability(word_freq_ns, words_pos_ns, words_neg_ns)

# Test samples
unseen_reviews = [
    "Beautiful, amazing movie, I loved it!",
    "Boring, not worth it",
    "Amazing, I liked it so much",
    "Annoying and boring",
    "No idea"
]

print("\n=== Classification WITH stopwords ===\n")
for review in unseen_reviews:
    positive, negative = classify(review, pos_reviews, neg_reviews, word_prob, remove_stopwords=False)
    print(f"Review: {review} -> Positive: {positive:.4f}, Negative: {negative:.4f}")

print("\n=== Classification WITHOUT stopwords ===\n")
for review in unseen_reviews:
    positive, negative = classify(review, pos_reviews_ns, neg_reviews_ns, word_prob_ns, remove_stopwords=True)
    print(f"Review: {review} -> Positive: {positive:.4f}, Negative: {negative:.4f}")
