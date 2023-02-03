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
        global type_trans
        global ciphered
        if ciphered!="" and type_trans=="encrypt__input":
            teks = "hasil enkripsi : "
            return render_template("vigenere.html", cipher=ciphered, text = teks)
        elif ciphered!="" and type_trans=="decrypt__input":
            teks = "hasil dekripsi : "
            return render_template("vigenere.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("vigenere.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        print(res.items(), file=sys.stderr)
        for key, value in res.items():
            if value!="encrypt__input" and value!="decrypt__input":
                inputs.append(value)
            else:
                type_trans = value
        
        print(inputs, file=sys.stderr)
        
        print(type_trans, file=sys.stderr)
        # print(arr_input, file=sys.stdout)
        if type_trans=="encrypt__input":
            ciphered = vigenere_cip(inputs[0], inputs[1], 'encrypt')
        elif type_trans=="decrypt__input":
            ciphered = vigenere_cip(inputs[0], inputs[1], 'decrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('vigenere'))

@app.route('/ext_vigenere', methods=['GET', 'POST'])
def ext_vigenere():
    if (request.method == 'GET'):
        global type_trans
        global ciphered
        if ciphered!="" and type_trans=="encrypt__input":
            teks = "hasil enkripsi : "
            return render_template("ext_vigenere.html", cipher=ciphered, text = teks)
        elif ciphered!="" and type_trans=="decrypt__input":
            teks = "hasil dekripsi : "
            return render_template("ext_vigenere.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("ext_vigenere.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        print(res.items(), file=sys.stderr)
        for key, value in res.items():
            if value!="encrypt__input" and value!="decrypt__input":
                inputs.append(value)
            else:
                type_trans = value
        
        print(inputs, file=sys.stderr)
        
        print(type_trans, file=sys.stderr)
        # print(arr_input, file=sys.stdout)
        if type_trans=="encrypt__input":
            ciphered = extended_vigenere(inputs[0], inputs[1], 'encrypt')
        elif type_trans=="decrypt__input":
            ciphered = extended_vigenere(inputs[0], inputs[1], 'decrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('ext_vigenere'))


@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    if (request.method == 'GET'):
        global type_trans
        global ciphered
        if ciphered!="" and type_trans=="encrypt__input":
            teks = "hasil enkripsi : "
            return render_template("playfair.html", cipher=ciphered, text = teks)
        elif ciphered!="" and type_trans=="decrypt__input":
            teks = "hasil dekripsi : "
            return render_template("playfair.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("playfair.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        print(res.items(), file=sys.stderr)
        for key, value in res.items():
            if value!="encrypt__input" and value!="decrypt__input":
                inputs.append(value)
            else:
                type_trans = value
        
        print(inputs, file=sys.stderr)
        
        print(type_trans, file=sys.stderr)
        # print(arr_input, file=sys.stdout)
        if type_trans=="encrypt__input":
            ciphered = encrypt_playfair(inputs[1], inputs[0])
        elif type_trans=="decrypt__input":
            ciphered = decrypt_playfair(inputs[1], inputs[0])
        # print(pred, file=sys.stdout)
    return redirect(url_for('playfair'))

@app.route('/autokey_vigenere', methods=['GET', 'POST'])
def autokey_vigenere():
    if (request.method == 'GET'):
        global type_trans
        global ciphered
        if ciphered!="" and type_trans=="encrypt__input":
            teks = "hasil enkripsi : "
            return render_template("autokey_vigenere.html", cipher=ciphered, text = teks)
        elif ciphered!="" and type_trans=="decrypt__input":
            teks = "hasil dekripsi : "
            return render_template("autokey_vigenere.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("autokey_vigenere.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        print(res.items(), file=sys.stderr)
        for key, value in res.items():
            if value!="encrypt__input" and value!="decrypt__input":
                inputs.append(value)
            else:
                type_trans = value
        
        print(inputs, file=sys.stderr)
        
        print(type_trans, file=sys.stderr)
        # print(arr_input, file=sys.stdout)
        if type_trans=="encrypt__input":
            ciphered = autokey_vigenere_cip(inputs[0], inputs[1], 'encrypt')
        elif type_trans=="decrypt__input":
            ciphered = autokey_vigenere_cip(inputs[0], inputs[1], 'decrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('autokey_vigenere'))

@app.route('/affine', methods=['GET', 'POST'])
def affine():
    if (request.method == 'GET'):
        global type_trans
        global ciphered
        if ciphered!="" and type_trans=="encrypt__input":
            teks = "hasil enkripsi : "
            return render_template("affine.html", cipher=ciphered, text = teks)
        elif ciphered!="" and type_trans=="decrypt__input":
            teks = "hasil dekripsi : "
            return render_template("affine.html", cipher=ciphered, text = teks)
        else:
            teks=""
            return render_template("affine.html", cipher="", text= teks)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        print(res.items(), file=sys.stderr)
        for key, value in res.items():
            if value!="encrypt__input" and value!="decrypt__input":
                inputs.append(value)
            else:
                type_trans = value
        
        print(inputs, file=sys.stderr)
        
        print(type_trans, file=sys.stderr)
        # print(arr_input, file=sys.stdout)
        if type_trans=="encrypt__input":
            ciphered = affine_cipher(inputs[0], int(inputs[1]), int(inputs[2]), 'encrypt')
        elif type_trans=="decrypt__input":
            ciphered = affine_cipher(inputs[0], int(inputs[1]), int(inputs[2]), 'decrypt')
        # print(pred, file=sys.stdout)
    return redirect(url_for('affine'))

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    return render_template('hill.html')



if __name__ == '__main__':
    app.run(debug=True)