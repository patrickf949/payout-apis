from flask import Blueprint
from flask.json import jsonify

from resources.flexpay.views import (
    banks, create, view_transaction, view_transactions, hook
)

flexpay = Blueprint(
    'flexpay', 
    __name__,
    url_prefix='/flexipay'
)

flexpay.add_url_rule(
    '/transactions', 
    view_func=create, 
    methods=['POST']
)
flexpay.add_url_rule(
    '/transactions/<transaction_id>', 
    view_func=view_transaction, 
    methods=['GET']
)
flexpay.add_url_rule(
    '/transactions', 
    view_func=view_transactions, 
    methods=['GET']
)
flexpay.add_url_rule(
    '/hook', 
    view_func=hook, 
    methods=['POST']
)

flexpay.add_url_rule(
    '/banks', 
    view_func=banks, 
    methods=['GET']
)

