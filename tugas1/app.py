from flask import Flask, render_template, request, redirect, url_for
from cipher import *
import sys

from flask import Flask
app = Flask(__name__)
ciphered = ""


@app.route('/')
def index():
    ciphered = ""
    return render_template('index.html')


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if (request.method == 'GET'):
        global ciphered
        if ciphered!="":
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
    if (request.method == 'GET'):
        global ciphered
        if ciphered!="":
            teks = "hasil enkripsi : "
            return render_template("ext_vigenere.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("ext_vigenere.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        
        for key, value in res.items():
            inputs.append(value)
        print(inputs)

        # print(arr_input, file=sys.stdout)
        ciphered = extended_vigenere(inputs[0], inputs[1], 'encrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('ext_vigenere'))

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    return render_template('playfair.html')

@app.route('/autokey_vigenere', methods=['GET', 'POST'])
def autokey_vigenere():
    return render_template('autokey_vigenere.html')

@app.route('/affine', methods=['GET', 'POST'])
def affine():
    return render_template('affine.html')

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    return render_template('hill.html')



if __name__ == '__main__':
    app.run(debug=True)