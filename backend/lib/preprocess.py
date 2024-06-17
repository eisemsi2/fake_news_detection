import pandas as pd
import numpy as np
import re
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import string
import os

current_dir = os.path.dirname(__file__)
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    text = re.sub(r'\d+', '', text)
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    lematizer = WordNetLemmatizer()
    text = ' '.join([lematizer.lemmatize(word) for word in text.split()])
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_df(texts):
    """
    Preprocesses a list of texts.

    Args:
    texts (list of str): List of input texts to preprocess.

    Returns:
    list of str: List of preprocessed texts.
    """
    processed_text = []
    for text in tqdm(texts):
        processed_text.append(preprocess_text(text))
    return processed_text

def train_and_export(df):
    """
    Trains a Logistic Regression model using TF-IDF features from text data and exports the model and vectorizer.

    Args:
    df (DataFrame): Pandas DataFrame containing 'title' (text) and 'class' (target) columns.
    """
    df['title'] = preprocess_df(df['title'].values)


    tfidf_vectorizer = TfidfVectorizer()
    tfidf_features = tfidf_vectorizer.fit_transform(df['title'])
    X_train, X_test, y_train, y_test = train_test_split(tfidf_features, df['class'], test_size=0.25)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    print(accuracy_score(y_test, model.predict(X_test)))
    print(classification_report(y_test, model.predict(X_test)))

    with open(current_dir+'/../models/model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

    with open(current_dir+'/../models/vectorizer.pkl', 'wb') as vectorizer_file:
        pickle.dump(tfidf_vectorizer, vectorizer_file)

def main():
    df = pd.read_csv(current_dir+'/../data_sets/News.csv')
    df1 = pd.DataFrame()
    df1['title'] = df['title']
    df1['class'] = df['class']
    # print(df1)
    df2 = pd.read_csv(current_dir +'/../data_sets/news.csv')
    df2['class'] = df2['label'].apply(lambda x: 0 if x == 'FAKE' else 1)
    df2['title'] = df2['text']
    df2 = df2.drop(['text'], axis=1)
    df2 = df2.drop(['label'], axis=1)
    df3 = pd.concat([df1, df2], axis=0)
    train_and_export(df3)

if __name__ == "__main__":
    main();

