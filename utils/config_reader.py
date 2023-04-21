import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('config/test_config.ini')
    return config[section][key]
