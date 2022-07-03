import os
import sys
import json
from black import main
import ipfshttpclient
from distutils.log import debug
from unicodedata import name
from mint_nft import mint_token
from flask import Flask, render_template, request, redirect, url_for


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
        artist = request.form.get('content2')
        description = request.form.get('content5')
        nft_file = request.files['file']  
        
        
        client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
        file_info = client.add(nft_file)
        nft_file_url = app.config['IPFS_FILE_URL'] + file_info['Hash']

                   
        NFT_info = {
            "name": title,
            "description": description,
            "image": nft_file_url,
            "attributes": [{}]
        }
        
        with open('nft_json.json', 'w') as nft_json:
            json.dump(NFT_info, nft_json, indent=7)
        
        print(nft_json)
        nft_json_info = client.add('nft_json.json')
        metadata_url = app.config['IPFS_FILE_URL'] + nft_json_info['Hash']
        print(metadata_url, nft_json_info['Hash'])
        os. remove('nft_json.json')

        opensea_url = mint_token(metadata_url)
        return redirect(url_for('.nft_info', metadata_url=opensea_url))
    
    return render_template("page_3.html")


@app.route("/nft_info")
def nft_info():
    _metadata = request.args['metadata_url']
    return render_template("page_2.html", _metadata=_metadata)


if __name__ == '__main__':
    app.run(debug=TRUE)
    