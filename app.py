# Arquivos dentro da pasta Backend estão compilados aqui dentro, como um único servidor efetuando tudo, não separado por arquivos.

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

# Model pro database.
class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.nome + ", " +\
            self.email + ", " + self.telefone
            
    # expressao da classe no formato json
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

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

  
# Run do API e db.
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  # criar tabelas
  db.create_all()

  # teste para add pessoa ao banco
  p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", telefone = "47 99012 3232")
  
  db.session.add(p1)
  db.session.commit()