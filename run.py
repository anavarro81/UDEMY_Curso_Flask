from my_app import app

# Ejecuta la apliación.
# La instancia app de Flash se crea en el archivo __init__.py de my_app
app.config.from_pyfile("config.py")
app.run()

