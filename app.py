from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/myproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Equipo, Modelo, Marca, Fabricante, Caracteristica, Stock, Proveedor, Accesorio

@app.route('/')
def index():
    return render_template('index.html')

# Gestión de Equipos
@app.route('/equipo', methods=['GET', 'POST'])
def manage_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        categoria = request.form['categoria']
        costo = request.form['costo']
        nuevo_equipo = Equipo(nombre=nombre, modelo=modelo, categoria=categoria, costo=costo)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('manage_equipo'))
    equipos = Equipo.query.all()
    return render_template('equipo.html', equipos=equipos)

@app.route('/equipo/editar/<int:id>', methods=['GET', 'POST'])
def editar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.modelo = request.form['modelo']
        equipo.categoria = request.form['categoria']
        equipo.costo = request.form['costo']
        db.session.commit()
        return redirect(url_for('manage_equipo'))
    return render_template('editar_equipo.html', equipo=equipo)

@app.route('/equipo/borrar/<int:id>')
def borrar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('manage_equipo'))

# Gestión de Modelos
@app.route('/modelo', methods=['GET', 'POST'])
def manage_modelo():
    if request.method == 'POST':
        nombre_modelo = request.form['nombre_modelo']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = Modelo(nombre_modelo=nombre_modelo, fabricante_id=fabricante_id)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('manage_modelo'))
    modelos = Modelo.query.all()
    return render_template('modelo.html', modelos=modelos)

@app.route('/modelo/editar/<int:id>', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    if request.method == 'POST':
        modelo.nombre_modelo = request.form['nombre_modelo']
        modelo.fabricante_id = request.form['fabricante_id']
        db.session.commit()
        return redirect(url_for('manage_modelo'))
    return render_template('editar_modelo.html', modelo=modelo)

@app.route('/modelo/borrar/<int:id>')
def borrar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    db.session.delete(modelo)
    db.session.commit()
    return redirect(url_for('manage_modelo'))

# Gestión de Marcas
@app.route('/marca', methods=['GET', 'POST'])
def manage_marca():
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']
        nueva_marca = Marca(nombre_categoria=nombre_categoria)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('manage_marca'))
    marcas = Marca.query.all()
    return render_template('marca.html', marcas=marcas)

@app.route('/marca/editar/<int:id>', methods=['GET', 'POST'])
def editar_marca(id):
    marca = Marca.query.get_or_404(id)
    if request.method == 'POST':
        marca.nombre_categoria = request.form['nombre_categoria']
        db.session.commit()
        return redirect(url_for('manage_marca'))
    return render_template('editar_marca.html', marca=marca)

@app.route('/marca/borrar/<int:id>')
def borrar_marca(id):
    marca = Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    return redirect(url_for('manage_marca'))

# Gestión de Fabricantes
@app.route('/fabricante', methods=['GET', 'POST'])
def manage_fabricante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais_origen = request.form['pais_origen']
        nuevo_fabricante = Fabricante(nombre=nombre, pais_origen=pais_origen)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('manage_fabricante'))
    fabricantes = Fabricante.query.all()
    return render_template('fabricante.html', fabricantes=fabricantes)

@app.route('/fabricante/editar/<int:id>', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    if request.method == 'POST':
        fabricante.nombre = request.form['nombre']
        fabricante.pais_origen = request.form['pais_origen']
        db.session.commit()
        return redirect(url_for('manage_fabricante'))
    return render_template('editar_fabricante.html', fabricante=fabricante)

@app.route('/fabricante/borrar/<int:id>')
def borrar_fabricante(id):
    fabricante = Fabricante.query.get_or_404(id)
    db.session.delete(fabricante)
    db.session.commit()
    return redirect(url_for('manage_fabricante'))

# Gestión de Características
@app.route('/caracteristica', methods=['GET', 'POST'])
def manage_caracteristica():
    if request.method == 'POST':
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        nueva_caracteristica = Caracteristica(tipo=tipo, descripcion=descripcion)
        db.session.add(nueva_caracteristica)
        db.session.commit()
        return redirect(url_for('manage_caracteristica'))
    caracteristicas = Caracteristica.query.all()
    return render_template('caracteristica.html', caracteristicas=caracteristicas)

@app.route('/caracteristica/editar/<int:id>', methods=['GET', 'POST'])
def editar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    if request.method == 'POST':
        caracteristica.tipo = request.form['tipo']
        caracteristica.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('manage_caracteristica'))
    return render_template('editar_caracteristica.html', caracteristica=caracteristica)

@app.route('/caracteristica/borrar/<int:id>')
def borrar_caracteristica(id):
    caracteristica = Caracteristica.query.get_or_404(id)
    db.session.delete(caracteristica)
    db.session.commit()
    return redirect(url_for('manage_caracteristica'))

# Gestión de Stocks
@app.route('/stock', methods=['GET', 'POST'])
def manage_stock():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        ubicacion = request.form['ubicacion']
        nuevo_stock = Stock(cantidad=cantidad, ubicacion=ubicacion)
        db.session.add(nuevo_stock)
        db.session.commit()
        return redirect(url_for('manage_stock'))
    stocks = Stock.query.all()
    return render_template('stock.html', stocks=stocks)

@app.route('/stock/editar/<int:id>', methods=['GET', 'POST'])
def editar_stock(id):
    stock = Stock.query.get_or_404(id)
    if request.method == 'POST':
        stock.cantidad = request.form['cantidad']
        stock.ubicacion = request.form['ubicacion']
        db.session.commit()
        return redirect(url_for('manage_stock'))
    return render_template('editar_stock.html', stock=stock)

@app.route('/stock/borrar/<int:id>')
def borrar_stock(id):
    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    return redirect(url_for('manage_stock'))

# Gestión de Proveedores
@app.route('/proveedor', methods=['GET', 'POST'])
def manage_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        nuevo_proveedor = Proveedor(nombre=nombre, contacto=contacto)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('manage_proveedor'))
    proveedores = Proveedor.query.all()
    return render_template('proveedor.html', proveedores=proveedores)

@app.route('/proveedor/editar/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('manage_proveedor'))
    return render_template('editar_proveedor.html', proveedor=proveedor)

@app.route('/proveedor/borrar/<int:id>')
def borrar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('manage_proveedor'))

# Gestión de Accesorios
@app.route('/accesorio', methods=['GET', 'POST'])
def manage_accesorio():
    if request.method == 'POST':
        tipo = request.form['tipo']
        compatible_modelo_id = request.form['compatible_modelo_id']
        nuevo_accesorio = Accesorio(tipo=tipo, compatible_modelo_id=compatible_modelo_id)
        db.session.add(nuevo_accesorio)
        db.session.commit()
        return redirect(url_for('manage_accesorio'))
    accesorios = Accesorio.query.all()
    return render_template('accesorio.html', accesorios=accesorios)

@app.route('/accesorio/editar/<int:id>', methods=['GET', 'POST'])
def editar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)
    if request.method == 'POST':
        accesorio.tipo = request.form['tipo']
        accesorio.compatible_modelo_id = request.form['compatible_modelo_id']
        db.session.commit()
        return redirect(url_for('manage_accesorio'))
    return render_template('editar_accesorio.html', accesorio=accesorio)

@app.route('/accesorio/borrar/<int:id>')
def borrar_accesorio(id):
    accesorio = Accesorio.query.get_or_404(id)
    db.session.delete(accesorio)
    db.session.commit()
    return redirect(url_for('manage_accesorio'))

if __name__ == '__main__':
    app.run(debug=True)
