from bottle import run
from src.server import *
from src.load_properties import get_host
from src.replace_url import replace_url

if __name__ == '__main__':
    replace_url()
    hst = get_host()
    run(host=hst, port=80, debug=False)
