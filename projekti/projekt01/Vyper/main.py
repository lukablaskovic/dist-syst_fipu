# pip install web3, eth_tester
from web3 import Web3

import json

with open("abi.json", "r") as file:
    abi = json.load(file)

# Dobiveno preko https://remix.ethereum.org/
# Potrebno je:
# - instalirati vyper ekstenziju,
# - stvoriti novi file (github.vy) i u njega kopirati kod iz smart-contract.py
# - compile-anje koda, natrag vraca ABI.json i adresu
# Deployanje koda putem https://remix.ethereum.org/
SC_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Check if the connection was successful
if w3.isConnected():
    print("Connected to Ganache! 😁")
else:
    print("Connection to Ganache failed! 🥲")

# First, we need to get a reference to the contract instance
# Then, we can call any of the contract's functions
contract = w3.eth.contract(abi=abi, address=SC_address)

# Function for calling add_entry method from smart contract


def add_entry(username, github_link, filename):
    result = contract.functions.add_entry(
        username, github_link, filename).call()
    return result

# Function for calling get_entry method from smart contract


def get_entry(entry_id):
    result = contract.functions.get_entry(
        entry_id).call()
    return result
