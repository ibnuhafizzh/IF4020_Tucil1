from flask import Flask, render_template, request, redirect, url_for
from vigenere import *
import sys

from flask import Flask
app = Flask(__name__)
ciphered = "ya"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if (request.method == 'GET'):
        global ciphered
        if ciphered!="ya":
            teks = "hasil enkripsi : "
            return render_template("vigenere.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("vigenere.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        
        for key, value in res.items():
            inputs.append(value)
        print(inputs)

        # print(arr_input, file=sys.stdout)
        ciphered = vigenere_cip(inputs[0], inputs[1], 'encrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('vigenere'))

@app.route('/ext_vigenere', methods=['GET', 'POST'])
def ext_vigenere():
    return render_template('ext_vigenere.html')

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    return render_template('playfair.html')




if __name__ == '__main__':
    app.run(debug=True)