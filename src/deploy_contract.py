import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware


'''in this python file I used web3.py library to deploying the contract
but it's easier to use brownie'''

def main():

    '''initialize abi and bytecode of nftMinter contract'''
    file = open('nftMinter.json')
    data = json.load(file)
    abi = data["abi"]
    bytecode = data["bytecode"]


    '''set wallet address and private key of our wallet account'''
    rinkeby_chain_id = 4
    private_key = os.getenv('PRIVATE_KEY')
    provider_url = os.getenv('WEB3_PROVIDER')
    wallet_address = '0x34Ba01fA02EDc80a4F2f2AaEE077faaf6d06E342'


    # connecting to the infura http provier and then create our contract 
    w3 = Web3(Web3.HTTPProvider(provider_url))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    nftMinter = w3.eth.contract(abi=abi, bytecode=bytecode)


    '''making transaction'''
    # 1. first we need to initalize the nonce of our new transaction then build trx
    nonce = w3.eth.getTransactionCount(wallet_address)
    trx = nftMinter.constructor().buildTransaction({'from': wallet_address, "nonce": nonce, "chainId": rinkeby_chain_id})

    # 2. sign the trx
    signed_trx = w3.eth.account.sign_transaction(trx, private_key=private_key)

    # 3. send the transactioin
    trx_hash = w3.eth.send_raw_transaction(signed_trx.rawTransaction)
    trx_recipt = w3.eth.wait_for_transaction_receipt(trx_hash)
    print(trx_recipt.contractAddress)
    return trx_recipt.contractAddress

