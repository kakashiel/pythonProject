#!/bin/sh

#Connect nodes
curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5001", "http://0.0.0.0:5002"]}' 0.0.0.0:5000/connect_node
curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5000", "http://0.0.0.0:5002"]}' 0.0.0.0:5001/connect_node
curl -X POST --header "Content-Type: application/json" -d '{"nodes": ["http://0.0.0.0:5000", "http://0.0.0.0:5001"]}' 0.0.0.0:5002/connect_node

#Mine some blocks
curl 0.0.0.0:5000/mine_block
curl 0.0.0.0:5000/mine_block
curl 0.0.0.0:5000/mine_block


curl 0.0.0.0:5001/mine_block

#Consensus
curl 0.0.0.0:5000/replace_chain
curl 0.0.0.0:5001/replace_chain
curl 0.0.0.0:5002/replace_chain

#Add transaction
curl -X POST --header "Content-Type: application/json" -d '{ "sender": "Raoul", "receiver": "Arnaud", "amount": 100}' 0.0.0.0:5002/add_transaction