from brownie import nftMinter, accounts
from dotenv import load_dotenv
load_dotenv()

def main():

    print('connecting to your metamask account ...')
    account = accounts.load('dev1')
    print(f'your development account is: {account}')

    print("deploying nftMinter contract ....")
    contract = nftMinter.deploy({'from': account}, publish_source = False)
    print(f'greate! your contract deployed at {contract}')
    print(type(contract))