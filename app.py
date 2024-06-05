from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Juan Pérez"
    matricula = "123456"
    grado = "10"
    grupo = "A"
    
    # HTML con estilo en línea para dar colores azules
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f8ff; /* Fondo azul claro */
                color: #00008b; /* Texto azul oscuro */
            }}
            .info {{
                padding: 10px;
                border: 2px solid #1e90ff; /* Borde azul */
                border-radius: 5px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                width: 50%;
                margin: auto;
                text-align: center;
            }}
            h1 {{
                color: #4682b4; /* Azul acero */
            }}
        </style>
    </head>
    <body>
        <div class="info">
            <h1>Información del Estudiante</h1>
            <p>Nombre: {nombre}</p>
            <p>Matrícula: {matricula}</p>
            <p>Grado: {grado}</p>
            <p>Grupo: {grupo}</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
