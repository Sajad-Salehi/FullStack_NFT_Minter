from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/login")
def connect_wallet():
    return render_template("page_1.html")

@app.route("/home")
def home_page():
    return render_template("page_2.html")

@app.route("/nftMinter")
def nft_minter():
    return render_template("page_3.html")

if __name__ == "__main__":
    app.run()
    