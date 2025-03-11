from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router route for Caesar cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for encrypting text using Caesar cipher
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar_cipher = CaesarCipher()

    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

# Route for decrypting text using Caesar cipher
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar_cipher = CaesarCipher()

    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
