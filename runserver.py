from flask import Flask
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_babel import Babel

from app.api import blueprint as api_bp, api, register_namespaces
from app.models import db
from configs import configs


jwt = JWTManager()
cors = CORS()
babel = Babel()

def create_app(config_name='dev'):
    app = Flask(__name__)
    
    # config the app
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)
    
    # register blueprint     
    app.register_blueprint(api_bp, url_prefix='/api')
    
    #register api namespaces
    register_namespaces()

    # config the database
    db.init_app(app)

    # config the json web token manager
    jwt.init_app(app)
    
    # config the cors
    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # init babel for localization
    babel.init_app(app)

    return app

#app = Flask(__name__)
app = create_app()
mysql = MySQL(app)
api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }

api.add_resource(Quotes, '/')


if __name__ == '__main__':
    app.run(debug=True, port=5002)