from distutils.debug import DEBUG
from flask import Config


class config:
    '''General configurations'''
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(config):
    '''Production Configuration'''
    DEBUG = True


class TestConfig(Config):
    '''Test config'''
    DEBUG = True


class DevConfig(Config):
    '''dev'''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}