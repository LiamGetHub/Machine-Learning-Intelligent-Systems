import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

# Download stopwords if not already available
nltk.download('stopwords')

# Load stopwords for English and Spanish
stop_words_en = set(stopwords.words('english'))
stop_words_es = set(stopwords.words('spanish'))


# Function to extract words from text (excluding stopwords)
def extract_words(text, stop_words):
    return [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]


# Function to load and process files
def load_file(file_name, stop_words):
    words = []
    total_lines = 0

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            words.extend(extract_words(line, stop_words))
            total_lines += 1

    return words, total_lines


# Function to calculate word frequency in positive and negative reviews
def calculate_word_frequency(words_in_positive, words_in_negative):
    frequency = {}

    for word in words_in_positive:
        frequency[word] = frequency.get(word, [0, 0])
        frequency[word][0] += 1

    for word in words_in_negative:
        frequency[word] = frequency.get(word, [0, 0])
        frequency[word][1] += 1

    return frequency


# Function to calculate word probability using Laplace smoothing
def calculate_word_probability(frequency, words_in_positive, words_in_negative):
    probability = {}

    vocab_size = len(frequency)
    total_positive = len(words_in_positive)
    total_negative = len(words_in_negative)

    for word in frequency:
        positive = (frequency[word][0] + 1) / (total_positive + vocab_size)
        negative = (frequency[word][1] + 1) / (total_negative + vocab_size)
        probability[word] = [positive, negative]

    return probability


# Function to classify a review
def classify(text, positive_reviews, negative_reviews, probability, stop_words):
    words = extract_words(text, stop_words)
    total_reviews = positive_reviews + negative_reviews

    prob_positive = positive_reviews / total_reviews
    prob_negative = negative_reviews / total_reviews

    for word in words:
        if word in probability:
            prob_positive *= probability[word][0]
            prob_negative *= probability[word][1]

    total_prob = prob_positive + prob_negative
    return (prob_positive / total_prob, prob_negative / total_prob)


# Load English and Spanish reviews
words_pos_en, pos_count_en = load_file("positive_reviews.txt", stop_words_en)
words_neg_en, neg_count_en = load_file("negative_reviews.txt", stop_words_en)

words_pos_es, pos_count_es = load_file("positive_reviews_es.txt", stop_words_es)
words_neg_es, neg_count_es = load_file("negative_reviews_es.txt", stop_words_es)

# Calculate frequencies and probabilities for both languages
word_freq_en = calculate_word_frequency(words_pos_en, words_neg_en)
word_prob_en = calculate_word_probability(word_freq_en, words_pos_en, words_neg_en)

word_freq_es = calculate_word_frequency(words_pos_es, words_neg_es)
word_prob_es = calculate_word_probability(word_freq_es, words_pos_es, words_neg_es)

# Test Spanish classification
unseen_reviews_es = [
    "Película increíble, la amé!",
    "Fue aburrida, no la recomiendo.",
    "Muy entretenida y divertida.",
    "Una pérdida de tiempo, horrible experiencia."
]

print("\nClasificación en Español\n")

for review in unseen_reviews_es:
    result = classify(review, pos_count_es, neg_count_es, word_prob_es, stop_words_es)
    pos_score, neg_score = result

    if abs(pos_score - neg_score) > 0.25:
        if pos_score > neg_score:
            print(f'"{review}" es {pos_score:.4f} positivo')
        else:
            print(f'"{review}" es {neg_score:.4f} negativo')
    else:
        print(f'"{review}" es neutral {pos_score:.4f} positivo, {neg_score:.4f} negativo')
