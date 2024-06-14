from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer('bert-base-nli-mean-tokens')

with open('verify_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


