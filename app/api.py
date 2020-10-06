from flask import Blueprint
from flask_restplus import Api, Namespace
from flask_jwt_extended import exceptions
import jwt
from functools import wraps
from flask_jwt_extended import get_jwt_claims, get_jwt_identity
from flask_babel import gettext


blueprint = Blueprint('api', __name__)
api = Api(blueprint, title=gettext("OLINFER API"), doc='/doc', description="Endpoints", validate=True, security=['apikey', {'oauth2': 'read'}], authorizations={'apikey':{'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}})


# lazy loading of namespaces
def register_namespaces():
    pass