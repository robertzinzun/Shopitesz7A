from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from modelo.DAO import db,Categoria,Usuario,Producto
from flask_login import LoginManager,current_user,login_required,login_user,logout_user

app=Flask(__name__,template_folder='../vista',static_folder='../static')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userShopitesz:Hola.123@localhost/Shopitesz_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message = u"! Debes iniciar sesión !"

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
@app.route('/')
def incio():
    #return '<h1> Bienvenido a la tienda en linea SHOPITESZ </h1>'
    return  render_template('comunes/principal.html')

@app.route('/productos/<int:id>')
def listarProductos(id):
    p=Producto()
    p=p.consultaIndividual(id)
    return p.nombre+':'+p.categoria.nombre+':'+str(p.categoria.idCategoria)
    #return render_template('productos/listado.html')
#seccion para los usuarios
@app.route('/usuarios/login',methods=['post'])
def validarUsuario():
    user=Usuario()
    email=request.form['email']
    password=request.form['password']
    user=user.validar(email,password)
    if user!=None:
        login_user(user)
        return render_template('comunes/principal.html')
    else:
        flash('!Datos de la sesión incorrectos!')
        return render_template('usuarios/login.html')
@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    logout_user()
    return redirect(url_for('login'))

@app.route('/usuarios/ingresar')
def login():
    if current_user.is_authenticated:
        return render_template('comunes/principal.html')
    else:
        return render_template('usuarios/login.html')

@app.route('/usuarios/nuevo')
def nuevoUsuario():
    return render_template('usuarios/nuevo.html')

@app.route('/usuarios/registrar',methods=['post'])
def registrarUsuario():
    user=Usuario()
    user.nombreCompleto=request.form['nombre']
    user.domicilio = request.form['domicilio']
    user.telefono = request.form['telefono']
    user.email = request.form['email']
    user.password = request.form['password']
    user.tipo = request.form['tipo']
    user.insertar()
    flash('Usuario registrado con exito')
    return redirect(url_for('nuevoUsuario'))


#fin de la sección de usuarios
#Seccion para las rutas de categorias
@app.route('/categorias')
def categorias():
    c=Categoria()
    categorias=c.consultaGeneral()
    return render_template('categorias/consulta.html',categorias=categorias)

@app.route('/categorias/nuevo')
@login_required
def nuevaCategoria():
    if current_user.is_authenticated and current_user.is_admin():
        return render_template('categorias/nuevo.html')
    else:
        abort(404)

@app.route('/categorias/ver/<int:id>')
@login_required
def consultarCategoria(id):
    if current_user.is_authenticated and current_user.is_admin():
        c = Categoria()
        return render_template('categorias/editar.html',categoria=c.consultaIndividual(id))
    else:
        abort(404)

@app.route('/categorias/guardar',methods=['post'])
@login_required
def editarCategoria():
    if current_user.is_authenticated and current_user.is_admin():
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
    else:
        abort(404)

@app.route('/categorias/agregar',methods=['post'])
@login_required
def agregarCategoria():
    if current_user.is_authenticated and current_user.is_admin():
        c=Categoria()
        c.nombre=request.form['nombre']
        c.foto=request.files['foto'].read()
        c.insertar()
        flash('Categoria registrada con exito')
        return render_template('categorias/nuevo.html')
    else:
        abort(404)

@app.route('/categorias/imagen/<int:id>')
def consultarImagenCategoria(id):
    c=Categoria()
    return c.consultaIndividual(id).foto
@app.route('/categorias/eliminar/<int:id>')
@login_required
def eliminarCategoria(id):
    if current_user.is_authenticated and current_user.is_admin():
        c=Categoria()
        c.eliminar(id)
        flash('Categoria eliminada con exito')
        return redirect(url_for('categorias'))
    else:
        abort(404)
# fin de la seccion de categorias

#seccion de errores
@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'),404

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)