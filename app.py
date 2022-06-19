from distutils.log import debug
from pickle import TRUE
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
        artist = request.form.get('content2')
        price = request.form.get('content3')
        description = request.form.get('content4')
        NFT_info = {
            'Title': title,
            'Artist': artist,
            'Price': price,
            'description': description
        }
        print(NFT_info)
        
    return render_template("page_3.html")

if __name__ == '__main__':
    app.run(debug=TRUE)
    