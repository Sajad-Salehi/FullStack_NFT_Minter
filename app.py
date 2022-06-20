from distutils.log import debug
from pickle import TRUE
import ipfshttpclient
import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route("/login")
def connect_wallet():
    return render_template("page_1.html")

@app.route("/home")
def home_page():
    return render_template("page_2.html")

@app.route("/nftMinter", methods=["GET", "POST"])
def nft_minter():
    
    if request.method == "POST":
        title = request.form.get('content1')
        artistName = request.form.get('content2')
        creator = request.form.get('content3')
        price = request.form.get('content4')
        description = request.form.get('content5')
        img = request.files['file']
                                
        NFT_info = {
            'Title': title,
            'Price': price,
            'Artist_name': artistName,
            'Creator_addrs': creator,
            'description': description
        }
        print(NFT_info)
    return render_template("page_3.html")


if __name__ == '__main__':
    app.run(debug=TRUE)
    