from flask import Flask,render_template

app=Flask(__name__,template_folder='../vista')

@app.route('/')
def incio():
    #return '<h1> Bienvenido a la tienda en linea SHOPITESZ </h1>'
    return  render_template('comunes/index.html')

@app.route('/productos')
def listarProductos():

    return render_template('productos/listado.html')

if __name__=='__main__':
    app.run(debug=True)