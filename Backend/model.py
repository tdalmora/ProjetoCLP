from server import db

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