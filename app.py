# Assignment 2 template code
# Jamiel Sheikh

# Resources:
# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
# https://www.w3schools.com/bootstrap/default.asp
# https://www.w3schools.com/bootstrap/bootstrap_buttons.asp


from flask import Flask, render_template, request
import urllib.request as req
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def show_main_page():
    return render_template('main.html')

@app.route("/trade")
def show_trade_screen():
    return render_template('trade.html')

@app.route("/blotter")
def show_blotter():
    return render_template('blotter.html')

@app.route("/pl")
def show_pl():
    return render_template('pl.html')

@app.route("/submitTrade",methods=['POST'])
def execute_trade():
    symbol = request.form['symbol']
    price = get_quote(symbol)

    # pull quote
    # calculate trade value
    # insert into blotter
    # calculate impact to p/l and cash
    return "You traded at " + price

# Used snippet of Bloomberg scraping as posted on Slack
def get_quote(symbol):
    url = 'https://www.bloomberg.com/quote/' + symbol + ':US'
    page = req.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text
    return price

if __name__ == "__main__":
    app.run()
