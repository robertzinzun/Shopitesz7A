from flask import Flask,render_template,request

app=Flask(__name__,template_folder='../vista',static_folder='../static')

@app.route('/')
def incio():
    #return '<h1> Bienvenido a la tienda en linea SHOPITESZ </h1>'
    return  render_template('comunes/index.html')

@app.route('/productos')
def listarProductos():

    return render_template('productos/listado.html')

@app.route('/usuarios/login',methods=['post'])
def login():
    email=request.form['email']
    return 'Validando la cuenta de usuario:'+email

@app.route('/usuarios/ingresar')
def ingresar():
    return render_template('usuarios/login.html')
#Seccion para las rutas de categorias
@app.route('/categorias')
def categorias():

    return render_template('categorias/consulta.html',categorias=categorias)

@app.route('/categorias/nuevo')
def nuevaCategoria():
    return render_template('categorias/nuevo.html')

@app.route('/categorias/editar')
def editarCategoria():
    nombre='Videojuegos'
    return render_template('categorias/editar.html',nombreCategoria=nombre)

# fin de la seccion de categorias
if __name__=='__main__':
    app.run(debug=True)