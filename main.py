import pandas as pd
import string
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Week 1 setup
nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

# Week 2: Sample dataset
data = {
    "text": [
        "Markets rise as investors react positively to earnings.",
        "Stock prices fell sharply due to inflation concerns.",
        "The financial outlook remains neutral amidst uncertainty.",
        "Company reports record profits, shares soar.",
        "Global markets tumble amid geopolitical tensions."
    ],
    "sentiment": ["positive", "negative", "neutral", "positive", "negative"]
}
df = pd.DataFrame(data)

# Week 2: Preprocessing function
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation and not char.isdigit()])
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    doc = nlp(" ".join(tokens))
    lemmas = [token.lemma_ for token in doc]
    return " ".join(lemmas)

df["cleaned_text"] = df["text"].apply(clean_text)

# Week 3: TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned_text"])
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Week 4: Label Encoding
le = LabelEncoder()
df["sentiment_encoded"] = le.fit_transform(df["sentiment"])

# Week 4: Save cleaned data and TF-IDF
df.to_csv("cleaned_data.csv", index=False)
tfidf_df.to_csv("tfidf_vectors.csv", index=False)

# Week 4: EDA - word count
df["word_count"] = df["cleaned_text"].apply(lambda x: len(x.split()))
print("Average Word Count:", df["word_count"].mean())

# Week 4: Visualization
word_counts = pd.Series(" ".join(df["cleaned_text"]).split()).value_counts().head(10)
word_counts.plot(kind='bar', title='Top 10 Frequent Words')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("word_frequency.png")
plt.show()
