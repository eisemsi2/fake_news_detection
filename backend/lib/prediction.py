import sys
import re
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer
import pickle
import os

current_dir = os.path.dirname(__file__)

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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <article>")
        sys.exit(1)

    with open(current_dir+'/../models/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open(current_dir+'/../models/vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    article = sys.argv[1]
    # print(article)
    preprocessed_article = [preprocess_text(article)]
    # print(preprocessed_article)
    vectorized_article = vectorizer.transform(preprocessed_article)
    prediction_proba = model.predict_proba(vectorized_article)[0][1]
    print(prediction_proba)
