from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/gatos')
def gatos():
    return render_template("gatos.html")

@app.route('/pajaros')
def pajaros():
    return render_template("pajaros.html")

@app.route('/perros')
def perros():
    return render_template("perros.html")


if __name__ == "__main__":
    app.run(debug=True)
