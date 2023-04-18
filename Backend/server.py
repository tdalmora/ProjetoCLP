from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Criadno API
app = Flask(__name__)
CORS(app)   # Interconectividade entre dispositivos.

path = os.path.dirname(os.path.abspath(__file__))   # Diretório do database
arquivobd = os.path.join(path, 'pessoas.db')

#  Configs do app
app.secret_key = "thaigolindo"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd # criar banco +path. sqlite significa banco na maquina.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

from view import *

# Run do API e db.
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  # criar tabelas
  db.create_all()

  # teste para add pessoa ao banco
  p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", telefone = "47 99012 3232")
  
  db.session.add(p1)
  db.session.commit()