import configparser


def load_config():
    config = configparser.RawConfigParser()
    config.read('./config/resources.properties')
    return config


def get_db_credentials():
    config = load_config()
    host = config.get('DataBase', 'database.host')
    user = config.get('DataBase', 'database.user')
    password = config.get('DataBase', 'database.password')
    return host, user, password
