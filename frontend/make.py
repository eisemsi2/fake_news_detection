import subprocess

def make():
    subprocess.run(["npm", "install"])
    subprocess.run(["npm", "run", "build"])
    subprocess.run(["npm", "start"])

if __name__ == "__main__":
    make()