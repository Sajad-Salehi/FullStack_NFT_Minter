import os
import json
from tkinter import OUTSIDE
import ipfshttpclient
from distutils.log import debug
from pickle import TRUE
from unicodedata import name
from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True
app.config.from_pyfile('config.py')

@app.route("/login")
def connect_wallet():
    return render_template("page_1.html")



@app.route("/nftMinter", methods=["GET", "POST", "PUT"])
def nft_minter():
    
    if request.method == "POST":
        
        title = request.form.get('content1')
        artistName = request.form.get('content2')
        creator = request.form.get('content3')
        price = request.form.get('content4')
        description = request.form.get('content5')
        nft_file = request.files['file']  
        
        
        client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
        file_info = client.add(nft_file)
        nft_file_url = app.config['IPFS_FILE_URL'] + file_info['Hash']

                   
        NFT_info = {
            'Title': title,
            'Price': price,
            'Artist_name': artistName,
            'Creator_addrs': creator,
            'Description': description,
            'Asset_url': nft_file_url
        }
        
        with open('nft_json.json', 'w') as nft_json:
            json.dump(NFT_info, nft_json, indent=7)
        
        print(nft_json)
        nft_json_info = client.add('nft_json.json')
        metadata_url = app.config['IPFS_FILE_URL'] + nft_json_info['Hash']
        print(metadata_url)
        os. remove('nft_json.json')
        
    
    return render_template("page_3.html")


if __name__ == '__main__':
    app.run(debug=TRUE)
    