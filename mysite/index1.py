from flask import Flask, render_template, request



# Inicializar Firebase
# Ruta al archivo JSON de Firebase


# Inicializar Flask
app = Flask(__name__)


# Página de Inicio
@app.route('/')
def home():
    return render_template('home.html')

# Página de Cursos
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

# Soporte
@app.route('/soporte')
def soporte():
    return render_template('soporte.html')

# Detalle de un curso
@app.route('/detalle_curso')
def detalle_curso():
    curso_id = request.args.get('id')  # Obtener parámetro 'id'
    return render_template('detalle_curso.html', curso_id=curso_id)

if __name__ == '__main__':
    app.run(debug=True)  # Cambiar a False en producción

