from flask import Blueprint
from flask.json import jsonify


from resources.flutterwave.views import (
    bank_branches, create_transfer, hook, view_transfer, 
    view_transfers, banks, wallet_balance
)

flutterwave = Blueprint(
    'flutterwave', 
    __name__,
    url_prefix='/flutterwave'
)

flutterwave.add_url_rule(
    '/transfers', 
    view_func=create_transfer, 
    methods=['POST']
)
flutterwave.add_url_rule(
    '/transfers/<transfer_id>', 
    view_func=view_transfer, 
    methods=['GET']
)
flutterwave.add_url_rule(
    '/transfers/<page>/page', 
    view_func=view_transfers,
    methods=['GET']
)
flutterwave.add_url_rule(
    '/hook', 
    view_func=hook, 
    methods=['POST']
)
flutterwave.add_url_rule(
    '/banks/<country>', 
    view_func=banks, 
    methods=['GET']
)
flutterwave.add_url_rule(
    '/banks/<bank_id>/branches', 
    view_func=bank_branches, 
    methods=['GET']
)
flutterwave.add_url_rule(
    '/balance', 
    view_func=wallet_balance, 
    methods=['GET']
)
