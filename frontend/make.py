import subprocess
import os

current_dir = os.path.dirname(__file__)

def make():
    os.chdir(current_dir)
    print("Building frontend")
    subprocess.run(["npm", "install"])
    subprocess.run(["npm", "run", "build"])
    # subprocess.run(["npm", "start"])

if __name__ == "__main__":
    make()