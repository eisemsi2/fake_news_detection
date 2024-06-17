import subprocess
import os

current_dir = os.path.dirname(__file__)

def install_dependencies():
    print("Installing dependencies")
    subprocess.run(["pip3", "install", "-r", current_dir+"/requirements.txt"])
    print("Dependencies installed\n")

def make_predict_model():
    print("Making predict model")
    subprocess.run(["python3", current_dir+"/lib/preprocess.py"])
    print("Predict model is ready\n")

def make_verify_model():
    print("Making verify model")
    subprocess.run(["python3", current_dir+"/lib/verifyarticlemodel.py"])
    print("Verify model is ready\n")

def make():
    install_dependencies()
    make_predict_model()
    make_verify_model()

if __name__ == "__main__":
    os.chdir(current_dir)
    os.makedirs("models", exist_ok=True)
    make()
    subprocess.run(["npm", "install"])
    # subprocess.run(["node", "server.js"])

