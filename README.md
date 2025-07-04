# SOC-ID-137  
**Summer of Code Project: Financial News Sentiment Classification**

This repository contains my work for the Summer of Code project, where I'm building a machine learning model to classify financial news articles based on sentiment — positive, negative, or neutral. The main goal is to explore how NLP techniques can help extract useful insights from financial text data.

---

## What I Knew Before Starting

At the beginning, I had only a basic understanding of Python — such as using variables, loops, conditionals, lists, and dictionaries. I had no prior experience with text data, machine learning, or natural language processing (NLP). This project helped me build those skills from scratch.

---

## What I've Learned So Far

### Week 1: Python Basics
I revised Python fundamentals and got more comfortable with basic coding. Resources I used:

- [freeCodeCamp Python video](https://youtu.be/kqtD5dpn9C8?si=2OBhsaMBJ8Cx1jNs)
- [GeeksForGeeks Python Basics](https://www.geeksforgeeks.org/python-basics/)
- [Kaggle Python Course](https://www.kaggle.com/learn/python)
- [How to Set Up Virtual Environments](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

This helped me set up my environment and start coding in Jupyter Notebooks or VS Code.

---

### Week 2: Introduction to NLP
I started learning how to work with text data using various libraries and techniques.

Topics covered:
- Tokenization
- Stopword removal
- Stemming and Lemmatization
- Introduction to `nltk`, `spaCy`, and `pandas`

Helpful resources:
- [NLP Crash Course](https://youtu.be/1FZ0A1QCMWc?si=snmDGToAel0_PX4y)
- [Text Cleaning Tutorial](https://youtu.be/WnGPv6HnBok)

---

### Week 3 & 4: Text Cleaning and TF-IDF
These weeks focused on deeper text preprocessing and feature extraction.

Topics covered:
- Text cleaning using regex
- Lowercasing, punctuation removal, etc.
- Lemmatization with spaCy
- TF-IDF vectorization using `scikit-learn`

Helpful resources:
- [spaCy 101 Guide](https://spacy.io/usage/spacy-101)
- [NLTK Book - Text Processing Chapter](https://www.nltk.org/book/ch03.html)
- [TF-IDF Guide - Towards Data Science](https://towardsdatascience.com/tf-idf-for-text-mining-illustrated-with-a-real-life-example-3e1334c273b8)
- [TF-IDF Vectorizer - YouTube](https://youtu.be/qvZSdDOc6gs)

Datasets explored:
- [Sentiment Analysis for Financial News (Kaggle)](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
- Financial PhraseBank dataset

---

## Project Structure
financial-news-sentiment/
├── README.md # This file
├── requirements.txt # List of Python libraries used
└── main.py # Final project script
## Current Status

I’ve completed Python basics and basic NLP concepts like preprocessing and TF-IDF vectorization.  
So far, I have:
- Cleaned and vectorized the data
- Encoded labels
- Built a simple Logistic Regression model for sentiment classification

Next, I plan to:
- Perform EDA (word frequency, word clouds)
- Try other models (like Naive Bayes)
- Evaluate using accuracy and F1-score

## How to Run the Code

```bash
# Step 1: Clone the repository
git clone https://github.com/vaishali8531/SOC-ID-137.git
cd SOC-ID-137

# Step 2: Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the script
python main.py
