"""
[Aplicación básica del microframework Flask de Python]
Author: Fortinux
Date: []
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #return "<H1>Hola Mundo!</H1>"
    return render_template("index.html")


@app.route("/servicios")
def servicios():
    #return "<H1>Dentro de la página de SERVICIOS!</H1>"
    return render_template("base.html")
   
   
@app.route("/contacto")
def contacto():
    #return "<H1>Dentro de la página de CONTACTOS!</H1>"
    return render_template("base.html")


@app.route("/admin")
def admin():
    #return "<H1>Dentro de la página de ADMINISTRADOR!</H1>"    
    return render_template("base.html")