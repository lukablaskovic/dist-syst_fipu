# pip install web3, eth_tester
from web3 import Web3

import json

with open("abi.json", "r") as file:
    abi = json.load(file)

# Dobiveno preko https://remix.ethereum.org/
# Potrebno je:
# - instalirati vyper ekstenyiju,
# - stvoriti novi file (github.vy) i u njega kopirati kod iz smart-contract.py
# - comiple-at kod te dobivenu adresu i ABI koristiti za pozivanje add_entry funkcije
SC_address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Check if the connection was successful
if w3.isConnected():
    print("Connected to Ganache! 😁")
else:
    print("Connection to Ganache failed! 🥲")

# First, we need to get a reference to the contract instance
# Then, we can call any of the contract's functions
contract = w3.eth.contract(abi=abi, address=SC_address)
result = contract.functions.add_entry(
    "lukablaskovic", "https://github.com/lukablaskovic/dist-syst").call()
