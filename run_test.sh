sudo apt-get update && apt-get install -y xvfb firefox
export PATH=$PATH:$(pwd)/drivers
python basic_test.py