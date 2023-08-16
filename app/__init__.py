#dependencia de flask
from flask import Flask
#dependencia de configuracion
from .config import Config 
#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
#dependencia de las migraciones
from flask_migrate import Migrate

#crear el objeto Flask
app = Flask(__name__)
#configuracion del objeto flask
app.config.from_object(Config)


#crear el objeto de Modelos:
db = SQLAlchemy(app)
#crear el objeto de migracion
migrate = Migrate(app, db)

#importar los modelos de .models
from .models import Cliente, Producto, Venta