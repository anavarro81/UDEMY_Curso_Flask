from flask import Blueprint, render_template
from my_app.product.model.products import PRODUCTS

# Importa el diccionario: PRODUCTS del modulo product, model, products. 
# Contiene los datos para las pruebas de recuperacion y muestra de datos. 





# Recibe como parametro el nombre de la vista y el nombre del ejecutale (__name__). 
product = Blueprint('product', __name__)

@product.route('/')
@product.route('/home')
def index():
    # Abre la página index.html y le enviamos como parametro='products' 
    # el diccionario de PRODUCTOS.      
    return render_template('products/index.html', products=PRODUCTS)
    

@product.route('/product/<int:id>')
def show(id):
    product = PRODUCTS.get(id)    
    return render_template('products/show.html', product=product)

@product.route('/filter/<int:id>')
def filter(id):
    product = PRODUCTS.get(id)    
    return render_template('products/filter.html', product=product)

@product.app_template_filter('iva')
def iva_filter(product):
    
    if product['price']:
        return product['price'] * .20 + product['price']
    
    return 'No se ha podido calcular el precio + iva del producto. '

