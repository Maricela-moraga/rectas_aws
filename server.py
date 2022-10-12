#Importación de flask_app
from flask_app import app

#Importación de controladores
from flask_app.controllers import users_controller, recipes_controller

#Ejecución de la app
if __name__=="__main__":
    app.run(debug=True)
