#dependencia de flask
from flask import Flask, render_template
#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
#dependencia de las migraciones
from flask_migrate import Migrate
#dependencia para fecha y hora del sistema
from datetime import datetime
#dependencias de wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#crear el objeto Flask
app = Flask(__name__)




#definir la 'cadena de conexion'(connectionstring)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ficha_2687340'

#crear el objeto de Modelos:
db = SQLAlchemy(app)

#crear el objeto de migracion
migrate = Migrate(app, db)

#crear formulario de registro de productos
class ProductosForm(FlaskForm):
    nombre = StringField('ingrese nombre producto')
    precio = StringField('ingrese precio producto')
    submit = SubmitField('Registrar Producto')



#crear los modelos:
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key = True )
    username = db.Column(db.String(120),
                        nullable = True)
    #relaciones SQL alchemy
    ventas = db.relationship('Venta' ,
                    backref = "cliente" ,
                    lazy = "dynamic")
    
    
    
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
    

#rutas:
@app.route('/productos',
           methods = ['GET' ,'POST'])
def productos():
    form = ProductosForm()
    if form.validate_on_submit():
        #creamos un nuevo PRoducto
        p = Producto(nombre = form.nombre.data,
                     precio=form.precio.data )
        db.session.add(p)
        db.session.commit()
        return "producto registrado"
    return render_template('nuevo_producto.html',
                     form = form)
    




    

    



