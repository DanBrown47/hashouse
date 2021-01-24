import flask
from flask import request,jsonify
import urllib.request
import json
import hashlib

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def md5_hash(stuff_in):
    hash = hashlib.md5(stuff_in.encode()).hexdigest()
    return hash

@app.route('/', methods=['GET'])
def home():
    # We will come back here later 
    return """
    <html> HEllo W0rlD <hello> 
    """

@app.route('/help', methods=['GET'])
    # We will come back here later 
def help():
    return jsonify({'All commands':'commands'})



@app.route('/stdhash/md5/', methods=['GET'])
def api_md5():
    string_in = request.args.get("query")
    res = md5_hash(string_in)
    return jsonify({'result': res})

@app.route('/stdhash/sha256/', methods=['GET'])
def api_md5():
    string_in = request.args.get("query")
    res = md5_hash(string_in)
    return jsonify({'result': res})



app.run()