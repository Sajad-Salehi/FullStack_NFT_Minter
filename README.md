# FullStack_NFT_Minter
<h3>I have created this full stack NFT Minter Dapp using Python, Flask, Solidity and IPFS that can help you to create your NFTs automatically and very fast</h3>

<br/><br/>
<p align="center">
<img src="https://github.com/Sajad-Salehi/FullStack_NFT_Minter/blob/main/image/home.png" width="500" height="300">
<img src="https://github.com/Sajad-Salehi/FullStack_NFT_Minter/blob/main/image/nft3.png" width="500" height="300">
</p>

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
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

Create a Virtual Environments
```bash
python3 -m virtualenv venv
```

Then active venv
```bash
cd venv/bin
source activate
```

After that you need install flask and web3.py
```bash
pip install web3
pip install flask
```

Or, in linux:
```bash
sudo apt install python3-flask
```

and finally you need to install ipfs http client 
```bash
pip install ipfshttpclient
```

# Usage
Clone this repository, and run this command to initalize ipfs:
```bash
ipfs dameon
```

Then go to src/config.py and set (IPFS_CONNECT_URL and IPFS_FILE_URL),
You also need to export your private_key and web_provider

after that you can deploy your contract with brownie or web3.py
it's up to you, the easiest way is to use brownie.

deploy using web3.py:
```bash
cd src
python3 deploy_contract.py
```

using brownie:
```bash
pipx install eth-brownie
cd contracts
brownie run scripts/deploy.py --network <>
```

greate! you've deployed the  smart contract now copy the contract address and put it in mint_nft.py
and finally you can run your dapp with this command:
```bash
cd src
flask run
```
