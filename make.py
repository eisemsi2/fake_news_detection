import subprocess

def make():
    subprocess.run(["./backend/make.py"])
    subprocess.run(["./frontend/make.py"])
