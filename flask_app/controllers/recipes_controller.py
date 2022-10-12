#Importamos Flask y lo que utilizamos de flask
from flask import render_template, request, redirect, session, flash

#Importamos la app
from flask_app import app

#Importamos los modelos que usaremos
from flask_app.models.users import User
from flask_app.models.recipes import Recipe

@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session: #comprobamos que inicia sesion
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    return render_template('new_recipe.html', user=user)

@app.route("/create/recipe", methods=["post"])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")

    #validamos la receta
    if not Recipe.valida_receta(request.form):
        return redirect("/new/recipe")

    #guardamos la receta
    Recipe.save(request.form)
    return redirect("/dashboard")

@app.route("/edit/recipe/<int:id>")
def edit_recipe(id):
    if 'user_id' not in session: #comprobamos que inicia sesion
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    #la instancia de la receta que se debe desplegar en editar en base a la ID que recibimos en la URL
    formulario_receta = {"id": id}
    recipe =Recipe.get_by_id(formulario_receta)

    return render_template('edit_recipe.html', user=user, recipe=recipe)


@app.route("/update/recipe", methods=["post"])
def update_recipe():
    if "user_id" not in session:
        return redirect("/")

    if not Recipe.valida_receta(request.form):
        return redirect("/edit/recipe/"+request.form['recipe.id'])
    
    Recipe.update(request.form)
    return redirect("/dashboard")

@app.route("/delete/recipe/<int:id>")
def delete_recipe(id):
    if 'user_id' not in session: #comprobamos que se inicia sesion
        return redirect('/')

    formulario_delete = {"id": id}
    Recipe.delete(formulario_delete)
    return redirect("/dashboard")

@app.route("/view/recipe/<int:id>")
def view_recipe(id):
    if 'user_id' not in session: #comprobamos que se inicia sesion
        return redirect('/')

    formulario = {"id": session['user_id']}
    user = User.get_by_id(formulario)

    formulario_receta = {"id": id}
    recipe =Recipe.get_by_id(formulario_receta)

    return render_template('show_recipe.html', user=user, recipe=recipe)