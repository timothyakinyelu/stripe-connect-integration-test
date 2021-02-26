import os


class BaseConfig:
    """ Base configuration class"""
    
    DEBUG=os.environ.get('DEBUG')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    WTF_CSRF_ENABLED=True


class DevelopmentConfig(BaseConfig):
    """ Development environment configurations"""
    
    TEMPLATES_AUTO_RELOAD=True
    STRIPE_PUBLIC_KEY=os.environ.get('STRIPE_API_KEY')
    STRIPE_SECRET_KEY=os.environ.get('STRIPE_SECRET_KEY')
    
    

app_config = {
    'development': DevelopmentConfig
}