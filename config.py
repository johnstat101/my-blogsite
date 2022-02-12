from distutils.debug import DEBUG
from flask import Config


class config:
    '''General configurations'''
    pass


class ProdConfig(config):
    '''Production Configuration'''
    pass


class TestConfig(Config):
    '''Test config'''


class DevConfig(Config):
    '''dev'''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}