#dependencia de flask
from flask import Flask
#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
#dependencia de las migraciones
from flask_migrate import Migrate
#dependencia para fecha y hora del sistema
from datetime import datetime

#crear el objeto Flask
app = Flask(__name__)

#definir la 'cadena de conexion'(connectionstring)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#crear el objeto de Modelos:
db = SQLAlchemy(app)

#crear el objeto de migracion
migrate = Migrate(app, db)

#crear los modelos:
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key = True )
    username = db.Column(db.String(120),
                        nullable = True)
    
    
class Producto(db.Model):
    #definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer , primary_key = True )
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))

class Venta(db.Model):
    #definir los atributos
    __tablename__="ventas"
    id = db.Column(db.Integer , primary_key = True )
    fecha = db.Column(db.DateTime ,
                       default = datetime.utcnow)
    #clave foránea:
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))



