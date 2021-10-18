import os
import json
from flask.json import jsonify
from flask import request
from requests import get, post
from uuid import uuid4

FL_KEY = os.getenv('FL_KEY')
base_url = 'https://api.flutterwave.com/v3'

def create_transfer():
    try:
        data = request.get_json()
        data['reference']=str(uuid4())
        transfer = post(
            url=f'{base_url}/transfers',
            json=data,
            headers={
                'Authorization':f'Bearer {FL_KEY}'
            },
        )
        return jsonify({
            'message':"create transfer",
            'data':transfer.json(),
            'status':True,
        })
    except Exception as error:
        return jsonify({
            'message': 'create transfer',
            'data': transfer.text,
            'error': error,
            'status': True,
        })


def view_transfer(transfer_id):
    try:
        transfer = get(
            url=f'{base_url}/transfers/{transfer_id}',
            headers={
                'Authorization':f'Bearer {FL_KEY}'
            },
        )
        return jsonify({
            'message': 'single transfer',
            'data':transfer.json(),
            'status': True,
        })
    except Exception as error:
        return jsonify({
            'message': 'single transfer',
            'error':error,
            'status': False,
        })


def view_transfers():
    try:
        transfer = get(
            url=f'{base_url}/transfers',
            headers={
                'Authorization':f'Bearer {FL_KEY}'
            },
        )
        return jsonify({
            'message': 'single transfer',
            'data': transfer.json(),
            'status': True,
        })
    except Exception as error:
        return jsonify({
            'message': 'single transfer',
            'error':error,
            'status': False,
        })


def hook():
    return jsonify({
        'message':'hook',
        'success':True,
    })

def banks(country='UG'):
    banks = get(
        url=f'{base_url}/banks/{country}',
        headers={
            'Authorization':f'Bearer {FL_KEY}'
        }
    ).json()
    return jsonify({
        'message':'banks',
        'banks':banks,
        'success':True,
    })


def bank_branches(bank_id):
    banks = get(
        url=f'{base_url}/banks/{bank_id}/branches',
        headers={
            'Authorization':f'Bearer {FL_KEY}'
        }
    ).json()
    return jsonify({
        'message':'banks',
        'banks':banks,
        'success':True,
    })
