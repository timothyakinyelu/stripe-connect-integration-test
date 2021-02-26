from flask import (
    Flask, 
    request, 
    current_app, 
    json, 
    make_response, 
    jsonify, 
    render_template
)
from src.helpers.load_config import loadConfig
from flask_wtf.csrf import CSRFProtect
import stripe


csrf = CSRFProtect()
def createApp():
    app = Flask(__name__, instance_relative_config=True, template_folder='./templates')
    mode = app.env
    Config = loadConfig(mode)
    app.config.from_object(Config)
    
    csrf.init_app(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    
    @app.route('/create-connected-account', methods=['GET', 'POST'])
    def createAccount():
        pass
    
    
    @app.route('/web_hook', methods=['POST'])
    @csrf.exempt
    def web_hook_events():
        # set stripe secret_key
        stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
        
        payload = request.json

        event = None
        
        try:
            event = stripe.Event.construct_from(
                payload, stripe.api_key
            )
        except ValueError as e:
            res = {'msg': str(e)}
            return make_response(jsonify(res), 400)
        

        # handle events
        if event.type == 'payment_intent.created':
            payment_intent = event.data.object #contains a stripe.PaymentIntenet object
            res = {'data': payment_intent}
            
            return make_response(jsonify(res), 200)
        elif event.type == 'payment_intent.method':
            payment_method = event.data.object #constains a stripe.PaymentMethod object
            res = {'data': payment_method}
            
            return make_response(jsonify(res), 200)
        else:
            print('Unhandled event type {}'.format(event.type))
                     
    
    with app.app_context():
        return app