from flask import Flask
from src.helpers.load_config import loadConfig
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()
def createApp():
    app = Flask(__name__, instance_relative_config=True)
    mode = app.env
    Config = loadConfig(mode)
    app.config.from_object(Config)
    
    csrf.init_app(app)
    
    @app.route('/')
    def index():
        return 'Hello World!'
    
    with app.app_context():
        return app