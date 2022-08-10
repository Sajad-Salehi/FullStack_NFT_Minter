# FullStack_NFT_Minter
<h3>Full stack NFT Minter Dapp using Python, Flask, Solidity and IPFS that can help you to create your NFTs automatically</h3>
<h5>What is a Minter NFT?
A simple UI where you can input a link to your digital asset, a title, and a description</h5>

<br/><br/>
<p align="center">
<img src="https://github.com/Sajad-Salehi/FullStack_NFT_Minter/blob/main/image/home.png" width="500" height="270">
<img src="https://github.com/Sajad-Salehi/FullStack_NFT_Minter/blob/main/image/nft3.png" width="500" height="270">
</p>

## Prerequisites

Please install or have installed the following:

- [python](https://www.python.org/downloads/)
- [metamask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjtl7Oi6N_4AhWei_0HHbjzDH4QjBB6BAgHEAE&url=https%3A%2F%2Fmetamask.io%2Fdownload%2F&usg=AOvVaw049ASZIf5umKu9KN8vjUeH)

## Installation

[Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), if you haven't already. Here is a simple way to install venv.

```bash
python -m pip install --user virtualenv
python -m virtualenv --help
```

Or, if that doesn't work, via pipx
```bash
pipx install virtualenv
virtualenv --help
```

Create a Virtual Environments and active venv
```bash
python3 -m virtualenv venv
cd venv/bin
source activate
```

After that you need install flask, web3.py and ipfs that we're going to use it to store our metadata 
```bash
pip install web3
pip install flask
pip install ipfshttpclient
pip install eth-brownie
```


# Usage
Run this command to initalize ipfs:
```bash
ipfs daemon 
export IPFS_CONNECT_URL= "Connect_url"
```

First clone this repo and after that, you need to deploy the smart contract with brownie or web3.py
it's up to you, the easiest way is to use brownie.

1. Deploy using web3.py:
```bash
cd src
python3 deploy_contract.py
```

2. Deploy using brownie:
''you can use other network instead of rinkeby''
```bash
cd contracts
brownie run scripts/deploy.py --network rinkeby
```

Now you need to set your private_key and web3_provider(use Infura or Alchemy)
```bash
export WEB3_PROVIDER= "Web3_provider"
export PRIVATE_KEY= "Private_key"
```

Then go to the src/mint_token.py, set your smart contract address 
and use this command to run the app
```bash
cd src
flask run
```

## Resources

To get started with Brownie:

* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).
* ["Getting Started with Flask"](https://flask.palletsprojects.com/en/2.1.x/quickstart/) a quickstart for flask
* ["Getting Started with IPFS"](https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10) getting started with python and ipfs
* ["Getting Started with web3.py"](https://medium.com/geekculture/interacting-with-ethereum-network-in-python-using-web3-py-part-4-73ee4c978626) web3.py quickstart
* ["Introduction to ERC721 standard"](https://medium.com/blockchannel/walking-through-the-erc721-full-implementation-72ad72735f3c) ERC721 standard tutrial
* ["OpenZeppelin libraries docs"](https://docs.openzeppelin.com/contracts/4.x/)OpenZeppelin contracts documentation

## License

This project is licensed under the [MIT license](LICENSE).
