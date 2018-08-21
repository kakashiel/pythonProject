import datetime
import hashlib
import json
import requests
import sys

from uuid import uuid4
from urllib.parse import urlparse
from flask import Flask, jsonify, request


#1- The  Palo IT crypto

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_chain = 1
        while block_chain < len(chain):
            block = chain[block_chain]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_chain += 1
        return True

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if max_length < length and self.is_chain_valid(chain):
                    longest_chain = chain
                    max_length = length
        if longest_chain:
            self.chain = longest_chain
            return True
        return False



#2- Mining blockchain


#Creating Web app
app = Flask(__name__)

#Creating an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')

#Create the blockchain
blockchain = Blockchain()


"""
    Exemple:
    curl 0.0.0.0:5000/mine_block
"""
@app.route('/mine_block', methods=['GET'])
def mine_block():
    start_time = datetime.datetime.now()
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender=node_address, receiver='Unknow', amount=10)
    block = blockchain.create_block(proof, previous_hash)
    end_time = datetime.datetime.now()
    response = {'message': 'Awsome, you mine a block!',
                'time': 'It take ' + str(end_time - start_time) + ' ms',
               'block': block}
    return jsonify(response), 200

"""
    Exemple:
    curl 0.0.0.0:5000/get_chain
"""
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

"""
    Exemple:
    curl 0.0.0.0:5000/is_valid
"""
@app.route('/is_valid', methods=['GET'])
def id_valid():
    if blockchain.is_chain_valid(blockchain.chain):
        response ={'Message': 'The ledger is valid'}
    else:
        response = {'Message': 'Seriously, dude, wtf is this ?!'}
    return jsonify(response), 200

"""
    Exemple:
    curl 0.0.0.0:5000/list_nodes
"""
@app.route('/list_nodes', methods=['GET'])
def list_nodes():
    response = {'Network': list(blockchain.nodes),
                'Number of nodes': len(list(blockchain.nodes))}
    return jsonify(response), 200

"""
    Exemple:
    curl -X POST --header "Content-Type: application/json" -d '{ "sender": "Raoul", "receiver": "Arnaud", "amount": 100}'\
    0.0.0.0:5002/add_transaction
"""

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all (key in json for key in transaction_keys):
        return "Some elements of the transaction are missing", 400
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    message ={'message': f'This  transaction will be added to block{index}'}
    return jsonify(message), 201

# Descentralized our blockchain
"""
    Exemple:
    curl --header "Content-Type: application/json" --request POST \
    --data '{"nodes": ["http://0.0.0.0:5001", "http://0.0.0.0:5002"]}' 0.0.0.0:5000/connect_node
"""
@app.route('/connect_node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)

    response = {'message': 'This nodes are now connected',
             'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

"""
    Exemple:
    curl 0.0.0.0:5000/replace_chain
"""
@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    if blockchain.replace_chain() is True:
        response ={'Message': 'The nodes had different chains so the chain was replaced by the longest one',
                   'new_chain': blockchain.chain}
    else:
        response = {'Message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        app.run(host='0.0.0.0', port=int(sys.argv[1]))
    else:
        app.run(host='0.0.0.0', port=5000)


"""

Demo

curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5001", "http://0.0.0.0:5002"]}' 0.0.0.0:5000/connect_node
curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5000", "http://0.0.0.0:5002"]}' 0.0.0.0:5001/connect_node
curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5000", "http://0.0.0.0:5001"]}' 0.0.0.0:5002/connect_node



TODO:
1- Function which periodicly adjust the difficulty
2-  A) Function which ask the permission to be add the list of nodes
    B) Function which periodicly connect to other nodes
3- Generate private key + public key + adress for user
4- Create wallet generator
5- Share mempool between nodes
6- UTXO manager
"""
