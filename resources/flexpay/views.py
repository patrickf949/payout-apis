from flask import json
from flask.json import jsonify
from requests import get, post


def create():
    return jsonify({
        'message':"create"
    })


def view_transaction(transaction_id):
    return jsonify({
        'message':'single transaction'
    })


def view_transactions():
    return jsonify({
        'message':'multiple transaction'
    })


def hook():
    return jsonify({
        'message':'hook'
    })


def banks():
    return jsonify({
        'message':'banks'
    })