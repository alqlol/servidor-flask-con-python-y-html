# Importa la clase Flask
from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la página principal
@app.route('/')
def index():
    # Renderiza la plantilla HTML
    return render_template('index.html')

# Ejecuta la aplicación en el puerto 8000
if __name__ == '__main__':
    app.run(port=8000)
