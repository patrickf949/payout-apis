from flask import json
from flask.json import jsonify
from requests import get, post


def create_transfer():
    return jsonify({
        'message':"create"
    })


def view_transfer(transfer_id):
    return jsonify({
        'message':'single transfer'
    })


def view_transfers():
    return jsonify({
        'message':'multiple transfers'
    })


def hook():
    return jsonify({
        'message':'hook'
    })


def banks():
    return jsonify({
        'message':'banks'
    })
