from flask import Flask, render_template, request, redirect, url_for
# from utils import *
import sys

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vignere', methods=['GET', 'POST'])
def vignere():
    return render_template('vignere.html')

@app.route('/ext_vignere', methods=['GET', 'POST'])
def ext_vignere():
    return render_template('ext_vignere.html')

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    return render_template('playfair.html')




if __name__ == '__main__':
    app.run(debug=True)