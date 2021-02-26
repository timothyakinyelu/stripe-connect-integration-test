from flask import Flask


def createApp():
    app = Flask(__name__, instance_relative_config=True)
    
    
    with app.app_context():
        return app