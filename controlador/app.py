from flask import Flask,render_template,request,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from modelo.DAO import db,Categoria,Usuario
from flask_login import LoginManager,current_user,login_required,login_user,logout_user

app=Flask(__name__,template_folder='../vista',static_folder='../static')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userShopitesz:Hola.123@localhost/Shopitesz_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
@app.route('/')
def incio():
    #return '<h1> Bienvenido a la tienda en linea SHOPITESZ </h1>'
    return  render_template('comunes/principal.html')

@app.route('/productos')
def listarProductos():

    return render_template('productos/listado.html')

@app.route('/usuarios/login',methods=['post'])
def validarUsuario():
    email=request.form['email']
    return 'Validando la cuenta de usuario:'+email

@app.route('/usuarios/ingresar')
def login():
    return render_template('usuarios/login.html')
#Seccion para las rutas de categorias
@app.route('/categorias')
def categorias():
    c=Categoria()
    categorias=c.consultaGeneral()
    return render_template('categorias/consulta.html',categorias=categorias)

@app.route('/categorias/nuevo')
def nuevaCategoria():
    return render_template('categorias/nuevo.html')

@app.route('/categorias/ver/<int:id>')
def consultarCategoria(id):
    c = Categoria()
    return render_template('categorias/editar.html',categoria=c.consultaIndividual(id))

@app.route('/categorias/guardar',methods=['post'])
def editarCategoria():
    c=Categoria()
    c.idCategoria=request.form['id']
    c.nombre=request.form['nombre']

    estatus=request.values.get('estatus',False)
    if estatus=="True":
        c.estatus=True
    else:
        c.estatus=False

    imagen=request.files['foto'].read()
    if imagen:
        c.foto=imagen
    c.actualizar()
    flash('Categoria editada con exito')
    return render_template('categorias/editar.html',categoria=c)

@app.route('/categorias/agregar',methods=['post'])
def agregarCategoria():
    c=Categoria()
    c.nombre=request.form['nombre']
    c.foto=request.files['foto'].read()
    c.insertar()
    flash('Categoria registrada con exito')
    return render_template('categorias/nuevo.html')

@app.route('/categorias/imagen/<int:id>')
def consultarImagenCategoria(id):
    c=Categoria()
    return c.consultaIndividual(id).foto
@app.route('/categorias/eliminar/<int:id>')
def eliminarCategoria(id):
    c=Categoria()
    c.eliminar(id)
    flash('Categoria eliminada con exito')
    return redirect(url_for('categorias'))
# fin de la seccion de categorias
if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)