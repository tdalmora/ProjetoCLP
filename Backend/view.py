from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from server import app, db
from models import *

# Rotas para a web
@app.route('/')
def home():
  return "<h1>Bem vindo a home</h1>"


@app.route('/lista')
def lista():
  # Pega do banco
  pessoas = db.session.query(Pessoa).first()
  
  # Usa o metodo json nesse objeto (1ue a gente mesmo criou)
  pessoas_em_json = pessoas.json()
  
  # Transoforma em json
  resposta = jsonify(pessoas_em_json)
  
  return resposta

# Exemplo de route com method post.
@app.route('/novo', methods=['POST'])
def novo():
  ...
