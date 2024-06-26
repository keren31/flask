from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Keren Joanna Garcia Zumaya"
    matricula = "20210661"
    grado = "9"
    grupo = "A"
    imagen_url = "https://github.com/keren31/flask/blob/master/yo.jpeg?raw=true"
    universidad_imagen_url = "https://github.com/keren31/flask/blob/master/uthh.jpg?raw=true"  # URL de ejemplo para la imagen de la universidad
    
    return f'''
    <html>
    <head>
        <style>
            @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f8ff; /* Fondo azul claro */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container-wrapper {{
                display: flex;
                justify-content: space-around;
                width: 90%;
            }}
            .container {{
                padding: 20px;
                border: 1px solid #1e90ff; /* Borde azul */
                border-radius: 10px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 300px;
                margin: 10px;
            }}
            .info-container {{
                text-align: left;
                flex: 2; /* Hace que el contenedor de información de la universidad sea más grande */
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}
            .info-container img {{
                align-self: flex-end;
                width: 150px;
                height: 150px;
                border-radius: 10px;
                margin-left: 10px;
            }}
            h1 {{
                color: #4682b4; /* Azul acero */
                margin-bottom: 20px;
            }}
            p {{
                color: #00008b; /* Texto azul oscuro */
                margin: 5px 0;
            }}
            .profile-img {{
                border-radius: 50%;
                width: 150px;
                height: 150px;
                margin-bottom: 20px;
            }}
            .social-icons a {{
                color: #1e90ff; /* Azul */
                text-decoration: none;
                margin: 0 10px;
                font-size: 24px;
            }}
            .social-icons a:hover {{
                color: #4682b4; /* Azul acero */
            }}
        </style>
    </head>
    <body>
        <div class="container-wrapper">
            <div class="container">
                <img src="{imagen_url}" alt="Profile Picture" class="profile-img">
                <h1>Información del Estudiante</h1>
                <p><strong>Nombre:</strong> {nombre}</p>
                <p><strong>Matrícula:</strong> {matricula}</p>
                <p><strong>Grado:</strong> {grado}</p>
                <p><strong>Grupo:</strong> {grupo}</p>
                <div class="social-icons">
                    <a href="https://www.facebook.com/keren.zumaya?mibextid=ZbWKwL" target="_blank"><i class="fab fa-facebook"></i></a>
                    <a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
                </div>
            </div>
            <div class="container info-container">
                <h1>Estudio en</h1>
                <p><strong>Universidad Tecnológica de la Huasteca Hidalguense</strong> </p>
                <p><strong>Dirección: </strong> Carr. Huejutla - Chalahuiyapa S/N, Col.Tepoxteco, 43000 Huejutla de Reyes, Hgo.</p>
                <p><strong>Teléfono:</strong> 789 896 2088</p>
                <img src="{universidad_imagen_url}" alt="Universidad">
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)




