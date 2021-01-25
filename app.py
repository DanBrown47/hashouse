import flask
from flask import request,jsonify
import urllib.request
import json
import hashlib

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET' , 'POST'])
def home():
    # We will come back here later 
    return """
    <html> HEllo W0rlD <hello> 
    """
@app.route('/help', methods=['GET' , 'POST'])
    # We will come back here later 
def help():
    return jsonify({'All commands':'commands'})



@app.route('/hash/md5/', methods=['GET' , 'POST'])
def api_md5():
    string_in = request.args.get("query")
    res = hashlib.md5(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'md5'})


# SHA Family 
@app.route('/hash/sha256/', methods=['GET' , 'POST'])
def api_sha256():
    string_in = request.args.get("query")
    res = hashlib.md5(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha256'})

@app.route('/hash/sha384/', methods=['GET' , 'POST'])
def api_sha384():
    string_in = request.args.get("query")
    res = hashlib.sha384(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha384'})

@app.route('/hash/sha224/', methods=['GET' , 'POST'])
def api_sha224():
    string_in = request.args.get("query")
    res = hashlib.sha224(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha224'})

@app.route('/hash/sha512/', methods=['GET' , 'POST'])
def api_sha512():
    string_in = request.args.get("query")
    res = hashlib.sha512(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha512'})

@app.route('/hash/sha1/', methods=['GET' , 'POST'])
def api_sha1():
    string_in = request.args.get("query")
    res = hashlib.sha1(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha1'})

@app.route('/hash/sha3_224/', methods=['GET' , 'POST'])
def api_sha3_224():
    string_in = request.args.get("query")
    res = hashlib.sha3_224(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha3_224'})

@app.route('/hash/sha3_256/', methods=['GET' , 'POST'])
def api_sha3_256():
    string_in = request.args.get("query")
    res = hashlib.sha3_256(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha3_256'})

@app.route('/hash/sha3_384/', methods=['GET' , 'POST'])
def api_sha3_384():
    string_in = request.args.get("query")
    res = hashlib.sha3_384(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha3_384'})

@app.route('/hash/sha3_512/', methods=['GET' , 'POST'])
def api_sha3_512():
    string_in = request.args.get("query")
    res = hashlib.sha3_512(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'sha3_512'})

#SHAKE FAMILY
@app.route('/hash/shake_256/', methods=['GET' , 'POST'])
def api_shake_256():
    string_in = request.args.get("query")
    size = int(request.args.get("size"))
    res = hashlib.shake_256(string_in.encode()).digest(size)
    return jsonify({'result': str(res),
                    'algo':'shake_265',
                    'size':size})

@app.route('/hash/shake_128/', methods=['GET' , 'POST'])
def api_shake_128():
    string_in = request.args.get("query")
    size = int(request.args.get("size"))
    res = hashlib.shake_128(string_in.encode()).digest(size)
    return jsonify({'result': str(res),
                    'algo':'shake_128',
                    'size':size})


#BLAKE FAMILY
@app.route('/hash/blake2s/', methods=['GET' , 'POST'])
def api_blake2s():
    string_in = request.args.get("query")
    res = hashlib.blake2s(string_in.encode()).hexdigest()
    return jsonify({'result': res,
                    'algo':'blake2s'})

@app.route('/hash/blake2b/', methods=['GET' , 'POST'])
def api_blake2b():
    string_in = request.args.get("query")
    res = hashlib.blake2b(string_in.encode()).digest()
    return jsonify({'result': str(res),
                    'algo':'blake2b'})


if __name__ == '__main__':
    app.run()
