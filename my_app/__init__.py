from flask import Flask
from my_app.product.views import product

app = Flask(__name__)

# Le pasamos la vista hello_word que hemos importado previamente. 
app.register_blueprint(product)

@app.template_filter('mayusculas')
def convertir_mayusculas(texto):
    return texto.upper()

@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n*2