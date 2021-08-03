#importar flask y crear la variable app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#conexico uri a la base de datos
#app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@localhost:3306/pyalmacen"
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)


#primero importar db y luego las vistas
#importar las vistas
from my_app.product.views import product
app.register_blueprint(product)

#cargar despues de las vistas
db.create_all()


#creación de un filtro
@app.template_filter('mydouble')
def reverse_filter(n:int):
    return n*2








