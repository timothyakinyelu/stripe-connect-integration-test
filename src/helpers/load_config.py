from instance.config import app_config, BaseConfig


def loadConfig(MODE):
    """ Load environment variables"""
    
    if MODE == 'development':
        return app_config['MODE']
    else:
        return BaseConfig