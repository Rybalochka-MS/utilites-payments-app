from bottle import run
from src.server import *

if __name__ == '__main__':
    run(host='ec2-3-122-158-250.eu-central-1.compute.amazonaws.com', port=80, debug=False)
