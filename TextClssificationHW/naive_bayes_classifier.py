from nltk import word_tokenize
from nltk.corpus import stopwords

class NaiveBayesClassifier:
    def __init__(self, class_files, language='english', include_stopwords=True):
        self.class_files = class_files
        self.language = language
        self.include_stopwords = include_stopwords
        self.stop_words = set(stopwords.words(language)) if include_stopwords else set()
        self.word_counts = {}
        self.class_counts = {}
        self.total_words = {}
        self.vocab = set()
        self._train()

    def extract_words(self, text):
        return [
            word.lower() for word in word_tokenize(text)
            if any(c.isalpha() for c in word) and word.lower() not in self.stop_words
        ]

    def load_file(self, file_name):
        words = []
        total_lines = 0
        
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                words.extend(self.extract_words(line))
                total_lines += 1
        
        return words, total_lines

    def _train(self):
        for category, file_name in self.class_files.items():
            words, total_lines = self.load_file(file_name)
            self.word_counts[category] = {}
            self.class_counts[category] = total_lines
            self.total_words[category] = len(words)
            
            for word in words:
                self.vocab.add(word)
                if word in self.word_counts[category]:
                    self.word_counts[category][word] += 1
                else:
                    self.word_counts[category][word] = 1
    
    def calculate_word_probability(self, word, category):
        return (
            (self.word_counts[category].get(word, 0) + 1) /
            (self.total_words[category] + len(self.vocab))
        )
    
    def classify(self, text):
        words = self.extract_words(text)
        total_reviews = sum(self.class_counts.values())
        class_probabilities = {}
        
        for category in self.class_files:
            class_probabilities[category] = self.class_counts[category] / total_reviews
            for word in words:
                class_probabilities[category] *= self.calculate_word_probability(word, category)
        
        total_prob = sum(class_probabilities.values())
        return {category: class_probabilities[category] / total_prob for category in class_probabilities}

# Example usage
class_files = {"positive": "positive_reviews.txt", "negative": "negative_reviews.txt"}
classifier = NaiveBayesClassifier(class_files, include_stopwords=False)

unseen_reviews = [
    "Beautiful, amazing movie, I loved it!",
    "Boring, not worth it",
    "Amazing, I liked it so much",
    "Annoying and boring",
    "No idea"
]

for review in unseen_reviews:
    result = classifier.classify(review)
    print(f"Review: '{review}' Classification: {result}")
