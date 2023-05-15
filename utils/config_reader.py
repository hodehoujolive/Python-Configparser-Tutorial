import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('config/test_config.ini')
    return config[section][key]

def read_config_section(section):
    config = configparser.ConfigParser()
    config.read('config/test_config.ini')
    return config[section]
