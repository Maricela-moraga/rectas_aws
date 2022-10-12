#Importar flask
from flask import Flask

#Inicializar app
app = Flask(__name__)

#declarar la llave secreta
app.secret_key = "super llave secreta"