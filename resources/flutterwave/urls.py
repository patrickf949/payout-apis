from flask import Blueprint
from flask.json import jsonify


from resources.flutterwave.views import (
    create, hook, view_transaction, 
    view_transactions, banks
)

flutterwave = Blueprint(
    'flutterwave', 
    __name__,
    url_prefix='/flutterwave'
)

flutterwave.add_url_rule(
    '/transactions', 
    view_func=create, 
    methods=['POST']
)
flutterwave.add_url_rule(
    '/transactions/transaction_id', 
    view_func=view_transaction, 
    methods=['GET']
)
flutterwave.add_url_rule(
    '/transactions', 
    view_func=view_transactions,
    methods=['GET']
)
flutterwave.add_url_rule(
    '/hook', 
    view_func=hook, 
    methods=['POST']
)
flutterwave.add_url_rule(
    '/banks', 
    view_func=banks, 
    methods=['GET']
)