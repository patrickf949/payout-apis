from flask import Blueprint
from flask.json import jsonify

from resources.flexpay.views import (
    banks, create_transfer, view_transfer, 
    view_transfers, hook
)

flexpay = Blueprint(
    'flexpay', 
    __name__,
    url_prefix='/flexipay'
)

flexpay.add_url_rule(
    '/transfers', 
    view_func=create_transfer, 
    methods=['POST']
)
flexpay.add_url_rule(
    '/transfers/<transfer_id>', 
    view_func=view_transfer, 
    methods=['GET']
)
flexpay.add_url_rule(
    '/transfers', 
    view_func=view_transfers, 
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

