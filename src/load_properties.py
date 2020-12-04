import configparser


def load_config():
    config = configparser.RawConfigParser()
    config.read('./properties/resources.properties')
    return config


def get_db_credentials():
    config = load_config()
    host = config.get('DataBase', 'database.host')
    user = config.get('DataBase', 'database.user')
    password = config.get('DataBase', 'database.password')
    return host, user, password


def get_url():
    config = load_config()
    protocol = 'http://'
    host = config.get('Server', 'server.host')
    port = ':80'
    url = protocol + host + port
    return url


def get_host():
    config = load_config()
    host = config.get('Server', 'server.host')
    return host
