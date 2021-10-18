import os
from flask.json import jsonify

from flask import Flask

from resources.flexpay import flexpay
from resources.flutterwave import flutterwave


app = Flask(__name__)
app.register_blueprint(flutterwave)
app.register_blueprint(flexpay)

@app.route('/get', methods=['GET'])
def get_route():
    return jsonify({
        "message":"hello world"
    })



if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG'))
