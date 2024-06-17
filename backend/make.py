import subprocess
import os

current_dir = os.path.dirname(__file__)

def make_predict_model():
    print("Making predict model")
    subprocess.run(["python3", current_dir+"/lib/preprocess.py"])
    print("Predict model is ready")

def make_verify_model():
    print("Making verify model")
    subprocess.run(["python3", current_dir+"/lib/verifyarticlemodel.py"])
    print("Verify model is ready")

def make():
    make_predict_model()
    make_verify_model()

if __name__ == "__main__":
    os.chdir(current_dir)
    os.makedirs("models", exist_ok=True)
    make()
    subprocess.run(["npm", "install"])
    # subprocess.run(["node", "server.js"])

