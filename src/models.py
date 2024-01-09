from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False,unique=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "name":self.name,
            "username": self.username
        }
    
class Event(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    lugar = db.Column(db.String(250))
    inicio = db.Column(db.Integer, nullable=False)
    final = db.Column(db.Integer, nullable=False)
    duracion = db.Column(db.Integer)
    descripcion = db.Column(db.String(250))
    privacidad1 = db.Column(db.Boolean)
    privacidad2 = db.Column(db.Boolean)
    privacidad3 = db.Column(db.Boolean)
    privacidad4 = db.Column(db.Boolean)
    requisitos1 = db.Column(db.Boolean)
    requisitos2 = db.Column(db.Boolean)
    requisitos3 = db.Column(db.Boolean)
    requisitos4 = db.Column(db.Boolean)
    organizador = db.ForeignKey("User.id",nullable=False)
    invitados = db.ForeignKey("Invitado.id",nullable=False)
    respuestas = db.ForeignKey("Respuesta.id",nullable=False)

class Invitado(db.Model):
    __tablename__='invitado'
    id = db.Column(db.Integer, primary_key=True)
    idEvento = db.ForeignKey("Event.id",nullable=False)
    idInvitado = db.ForeignKey('User.id',nullable=False)

class Respuesta(db.Model):
    __tablename__='respuesta'
    id = db.Column(db.Integer, primary_key=True)
    idEvento = db.ForeignKey('Event.id',nullable=False)
    idInvitado = db.ForeignKey('User.id',nullable=False)
    status = db.Column(db.Integer,nullable=False) #0 prendiente, 1 Respondido, 2 Rechazado

