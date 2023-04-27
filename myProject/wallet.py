from web3 import Web3

# NB in questo progetto le transazioni vengono effettuate sulla tesntet Goerli anzichè Ropsten perchè quest'ultima è deprecata e i relativi faucet non sono più funzionanti

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/04fcb7b9f98b4eec99bb1d4ab137d7d3'))
account = w3.eth.account.create()
privateKey = account._private_key.hex()
address = account.address

print(f'Your address: {address}\nYour Key: {privateKey}')