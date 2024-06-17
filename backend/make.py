import subprocess
import os

def make_predict_model():
    print("Making predict model")
    subprocess.run(["python3", "./lib/preprocess.py"])
    print("Predict model is ready")

def make_verify_model():
    print("Making verify model")
    subprocess.run(["python3", "./lib/verifyarticlemodel.py"])
    print("Verify model is ready")

def make():
    make_predict_model()
    make_verify_model()

if __name__ == "__main__":
    os.makedirs("./models", exist_ok=True)
    make()
    subprocess.run(["npm", "install"])

