from sentence_transformers import SentenceTransformer
import pickle
import os

current_dir = os.path.dirname(__file__)
model = SentenceTransformer('bert-base-nli-mean-tokens')

with open(current_dir+'/../models/verify_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


