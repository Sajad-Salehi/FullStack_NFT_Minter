from distutils.log import debug
from pickle import TRUE
import ipfshttpclient
import json
import os
from flask import Flask, render_template, request
from flask import *  
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.debug = True

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
        nft_file_url = ""
        
        client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
        filename = secure_filename(nft_file.filename)
        print(filename)
        '''nft_file.save(os.path.join(app.config['UPLOAD_FOLDER']))'''
        x = client.add(nft_file)
        print(x)              
        NFT_info = {
            'Title': title,
            'Price': price,
            'Artist_name': artistName,
            'Creator_addrs': creator,
            'description': description,
            'file_url': nft_file_url
        }
        
    return render_template("page_3.html")


if __name__ == '__main__':
    app.run(debug=TRUE)
    