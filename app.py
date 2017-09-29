from flask import Flask
from datetime import datetime
app = Flask(__name__)
import urllib.request
import json

@app.route('/')
def homepage():

    price = json.loads((urllib.request.urlopen("http://api.fixer.io/latest?symbols=USD").read()))
    
    return """
    <H1>Price of EURUSD</H1>
    <p>It is currently {price}.</p>

    """.format(price = price['rates']['USD'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    


