from brownie import nftMinter, accounts

def test_contract():

    account = accounts.load('dev1')
    contract_address = nftMinter[-1]
    metadataURI = "https://ipfs.io/ipfs/QmeFcH8ULncAhzxxNgtbRbA5Usj7wHnjgySa2tMRqQiYDb"
    
    trx = contract_address.mintNFT(account, metadataURI, {'from': account})
    trx.wait(1)
    print(trx)
