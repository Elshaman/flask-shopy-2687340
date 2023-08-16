class Config:
    #definir la 'cadena de conexion'(connectionstring)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask-shopy-2687340'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'loqueudquiera'