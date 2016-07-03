"""
Solution to sharoonthomas's fulfil.io challenge.
Created on July 2, 2016
"""

from flask import Flask, render_template
app = Flask(__name__)



# tutorial routes

@app.route("/")
def hello():
    return( "Hello world!" )

@app.route("/dashboard")
def dashboard():
    # we get the data from a JSON web service and prepare it for display

    import requests
    import json

    # grabbing JSON from a static test URL because I don't have access to fulfil.io
    data = requests.get("https://dl.dropboxusercontent.com/u/42080340/response.json")
    recs = json.loads(data.content.decode())

    # here we tally the data we'll be plotting
    from collections import Counter
    states = Counter( [r["shipment_address.subdivision.code"] for r in recs] )
    # format the "data table" as a text string so I don't have to do it in Jinja2
    jslist = ",".join([ "['{}', {}]".format(i[0],i[1]) for i in states.items()])
    
    return render_template("dashboard.html",jslist=jslist)

    

    
import os
if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)