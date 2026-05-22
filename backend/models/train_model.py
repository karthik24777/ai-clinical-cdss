from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# better balanced dataset example
data = [
    ("fever cough cold", "flu"),
    ("high fever body pain", "dengue"),
    ("chest pain sweating", "heart_attack"),
    ("vomiting diarrhea dehydration", "food_poisoning"),
    ("headache nausea light_sensitivity", "migraine"),
    ("fever cough", "cold"),
    ("sneezing runny_nose", "allergy")
]

X = [i[0] for i in data]
y = [i[1] for i in data]

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X, y)