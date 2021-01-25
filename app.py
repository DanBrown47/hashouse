import flask
from flask import render_template, request,jsonify
import urllib.request
import json
import hashlib
import base64

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET' , 'POST'])
def home():
    return render_template("home.html")


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
    return jsonify({'result': str(res),
                    'algo':'blake2s'})

@app.route('/hash/blake2b/', methods=['GET' , 'POST'])
def api_blake2b():
    string_in = request.args.get("query")
    res = hashlib.blake2b(string_in.encode()).digest()
    return jsonify({'result': str(res),
                    'algo':'blake2b'})

##########  Hash  ###########
#########   Encoding #######

@app.route('/base64/encode/', methods=['GET' , 'POST'])
def base64_encode():
    string_in = request.args.get("query")
    string_bytes = string_in.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    res  = base64_bytes.decode('ascii')
    return jsonify({'result': str(res),
                    'algo':'base64_encoding'})

@app.route('/base64/decode/', methods=['GET' , 'POST'])
def base64_decode():
    base64_in = request.args.get("query")
    base64_bytes = base64_in.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    res  = message_bytes.decode('ascii')
    return jsonify({'result': str(res),
                    'algo':'base64_decode'})

if __name__ == '__main__':
    app.run()
