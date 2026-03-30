from flask import Flask, request, jsonify
from cipher.railfence.railfence_cipher import RailFenceCipher
app = Flask(__name__) 

#Railfence
railfence_cipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = int(data['key'])
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(text, key)})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = int(data['key'])
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(text, key)})