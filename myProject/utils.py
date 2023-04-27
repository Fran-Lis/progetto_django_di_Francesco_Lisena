from web3 import Web3

# NB in questo progetto le transazioni vengono effettuate sulla tesntet Goerli anzichè Ropsten perchè quest'ultima è deprecata e i relativi faucet non sono più funzionanti

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/04fcb7b9f98b4eec99bb1d4ab137d7d3'))
    address = '0x93a589886995e0dCcafAcCafd8f56810dD6bD3d1'
    privateKey = '0xd68a10ecc7e9adf0541873b0f488490cacb3aad8a1739f3a49d38dba0c25eb6e'
    nonce = w3.eth.get_transaction_count(address)
    gasPrice = w3.eth.gas_price
    value = w3.to_wei(0, 'ether')
    signedTx= w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice, 
        gas=100000, 
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.send_raw_transaction(signedTx.rawTransaction)
    txId = w3.to_hex(tx)
    return txId