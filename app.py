from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Keren Joanna Garcia Zumaya"
    matricula = "20210661"
    grado = "9"
    grupo = "A"
    
    # HTML con estilo en línea para dar colores azules
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f8ff; /* Fondo azul claro */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                padding: 20px;
                border: 1px solid #1e90ff; /* Borde azul */
                border-radius: 10px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 300px;
            }}
            h1 {{
                color: #4682b4; /* Azul acero */
                margin-bottom: 20px;
            }}
            p {{
                color: #00008b; /* Texto azul oscuro */
                margin: 5px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Información del Estudiante</h1>
            <p><strong>Nombre:</strong> {nombre}</p>
            <p><strong>Matrícula:</strong> {matricula}</p>
            <p><strong>Grado:</strong> {grado}</p>
            <p><strong>Grupo:</strong> {grupo}</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

