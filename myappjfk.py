from flask import Flask, jsonify

myappjfk = Flask(__name__)

pcs = [
    {'id': 1, 'marque': 'HP'},
    {'id': 2, 'marque': 'SAMSOUNG'}
]

users = [
    {'id': 1, 'name': 'KALALA'},
    {'id': 2, 'name': 'NGANDU'}
]

@myappjfk.route('/pcs', methods=['GET'])
def get_pcs():
    return jsonify({'pcs': pcs})

@myappjfk.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

if __name__ == '__main__':
    myappjfk.run(host='0.0.0.0', port=9000, debug=True)