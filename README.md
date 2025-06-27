# SOC-ID-137
summer of code project

This repository contains my work for the Summer of Code project, where I'm building a machine learning model to classify financial news articles based on sentiment — positive, negative, or neutral. The main goal is to explore how NLP techniques can help extract useful insights from financial text data.

What I Knew Before Starting
At the beginning, I had only a basic understanding of Python — such as using variables, loops, conditionals, lists, and dictionaries. I had no prior experience with text data, machine learning, or natural language processing (NLP). This project helped me build those skills from scratch.

What I've Learned So Far
Week 1: Python Basics
I revised Python fundamentals and got more comfortable with basic coding. Resources I used:

freeCodeCamp Python video

GeeksForGeeks Python Basics

Kaggle Python Course

How to Set Up Virtual Environments

This helped me set up my environment and start coding in Jupyter Notebooks.

Week 2: Introduction to NLP
I started learning how to work with text data using various libraries and techniques.

Topics covered:

Tokenization

Stopword removal

Stemming and Lemmatization

Introduction to nltk, spaCy, and pandas

I also watched crash courses on NLP pipelines and implementation:

NLP Crash Course

Text Cleaning Tutorial

Week 3 & 4: Text Cleaning and TF-IDF
These weeks focused on deeper text preprocessing and feature extraction.

Topics covered:

Cleaning text with regex

Preprocessing using nltk and spaCy

Lowercasing, punctuation removal, etc.

TF-IDF vectorization using scikit-learn

Some useful resources:

spaCy 101 Guide

NLTK Book - Text Processing Chapter

Regex Text Cleaning Tutorial

TF-IDF Concept - Towards Data Science

TF-IDF in Python - YouTube

Datasets I'm exploring:

Sentiment Analysis for Financial News (Kaggle)

Financial PhraseBank dataset


### Project Structure (Work in Progress)

```
financial-news-sentiment/
│
├── data/                      # Dataset files
├── notebooks/                 # Jupyter notebooks
│   ├── 01_preprocessing.ipynb
│   └── 02_tfidf_vectorization.ipynb
├── models/                    # Trained models (to be added)
├── README.md                  # This file
├── requirements.txt           # Package list
└── main.py                    # Final script version (optional)
```

Current Status
I’ve completed Python basics and basic NLP concepts like preprocessing and vectorization. I’m currently working on:

Finalizing text cleaning

Implementing TF-IDF

Exploring datasets

Next, I plan to:

Begin exploratory data analysis (EDA)

Train baseline models (Logistic Regression, Naive Bayes)

Evaluate performance using accuracy and F1-score



### How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/vaishali8531/SOC-ID-137.git

# Step 2: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Step 3: Install the required packages
pip install -r requirements.txt
```


