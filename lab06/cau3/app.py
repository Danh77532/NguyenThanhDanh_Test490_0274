from flask import Flask, render_template, request
# Đảm bảo đường dẫn import này khớp với cấu trúc thư mục của bạn
from cipher.railfence.railfence_cipher import RailFenceCipher

# BƯỚC QUAN TRỌNG: Khởi tạo đối tượng app
app = Flask(__name__)

# --------------------- ROUTES RAILFENCE ---------------------
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/decrypted text: {decrypted_text}"


# BƯỚC QUAN TRỌNG: Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)