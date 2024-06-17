import sys
import time
import pickle
import os
start_time = time.time()
current_dir = os.path.dirname(__file__)

with open(current_dir+'/../models/verify_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python verifyarticle.py <article1> <article2>")
        sys.exit(1)
    
    article1 = sys.argv[1]
    article2 = sys.argv[2]
    embedding = model.encode([article1, article2])
    similarities = model.similarity(embedding,embedding)
    end_time = time.time()
    # print("Time taken: ", end_time - start_time)
    print(similarities[0,1].item())
