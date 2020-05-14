from bottle import run
from src.server import *
from src.sql.create_db import create_db

if __name__ == '__main__':
    create_db()
    run(host='localhost', port=8080, debug=True)
