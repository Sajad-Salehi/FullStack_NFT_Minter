import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware



def mint_token(metadata_url):

    '''initialize abi of nftMinter contract'''
    file = open('nftMinter.json')
    data = json.load(file)
    abi = data["abi"]


    '''set wallet address and private key of our wallet account'''
    rinkeby_chain_id = 4
    private_key = os.getenv('PRIVATE_KEY')
    provider_url = os.getenv('WEB3_PROVIDER')
    wallet_address = '0xB268C07881a418D0BcADCF7204CeBc6D68A54904'


    # connecting to the infura http provier and create contract
    w3 = Web3(Web3.HTTPProvider(provider_url))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    nonce = w3.eth.getTransactionCount(wallet_address)
    contract_address = '0x7Ae397423c211B0B53914cd1610293bB3962ade6'
    Nft_Minter = w3.eth.contract(address=contract_address, abi=abi)


    # 1. make a transaction
    create_nft = Nft_Minter.functions.mintNFT(metadata_url).buildTransaction(
        {
            "chainId": rinkeby_chain_id,
            "from": wallet_address,
            "nonce": nonce
        })


    # 2. sign the transaction
    sign_create_nft = w3.eth.account.sign_transaction(
        create_nft,
        private_key=private_key)


    # 2. send the trnsaction
    trx_hash = w3.eth.send_raw_transaction(sign_create_nft.rawTransaction)
    trx_recipt = w3.eth.wait_for_transaction_receipt(trx_hash)
    token_id = Nft_Minter.functions.getItemId().call() 

    opensea_url = f"https://testnets.opensea.io/assets/rinkeby/{contract_address}/{token_id - 1}"
    print(opensea_url)
    return opensea_url



