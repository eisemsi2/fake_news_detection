import subprocess

def make():
    subprocess.run(["python3" , "./backend/make.py"])
    subprocess.run(["python3", "./frontend/make.py"])

if __name__ == "__main__":
    make()