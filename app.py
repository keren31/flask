from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Keren Joanna Garcia Zumaya"
    matricula = "20210661"
    grado = "9"
    grupo = "A"
    imagen_url = "https://github.com/keren31/flask/blob/master/yo.jpeg"  # URL directa de la imagen
    imagen_escuela_url = "https://lh3.googleusercontent.com/p/AF1QipNxAQeBQWYSSYyHI9ATEOTuuzhgkXJygHmb-mkz=s1360-w1360-h1020"  # URL directa de la imagen de la escuela
    
    return f'''
    <html>
    <head>
        <style>
            @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f8ff; /* Fondo azul claro */
                display: flex;
                flex-direction: column;
                align-items: center;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                display: flex;
                align-items: center;
                padding: 20px;
                border: 1px solid #1e90ff; /* Borde azul */
                border-radius: 10px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 80%;
                margin-bottom: 20px;
            }}
            .container .info {{
                margin-left: 20px;
            }}
            .container img {{
                border-radius: 50%;
                width: 150px;
                height: 150px;
            }}
            h1 {{
                color: #4682b4; /* Azul acero */
                margin-bottom: 20px;
            }}
            p {{
                color: #00008b; /* Texto azul oscuro */
                margin: 5px 0;
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
            .school-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
                border: 1px solid #1e90ff; /* Borde azul */
                border-radius: 10px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 80%;
                margin-bottom: 20px;
            }}
            .school-container img {{
                border-radius: 10px;
                width: 150px;
                height: 150px;
            }}
            .contact-form {{
                padding: 20px;
                border: 1px solid #1e90ff; /* Borde azul */
                border-radius: 10px;
                background-color: #e6f2ff; /* Fondo azul claro para el contenedor */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 80%;
            }}
            .contact-form input, .contact-form textarea {{
                width: calc(100% - 22px); /* Para considerar el padding */
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #1e90ff;
                border-radius: 5px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .contact-form button {{
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #1e90ff;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
            }}
            .contact-form button:hover {{
                background-color: #4682b4;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{imagen_url}" alt="Profile Picture">
            <div class="info">
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
        </div>
        <div class="school-container">
            <div class="school-info">
                <h1>Información de la Escuela</h1>
                <p><strong>Nombre:</strong> Escuela Platón</p>
                <p><strong>Dirección:</strong> Calle Falsa 123, Ciudad</p>
                <p><strong>Teléfono:</strong> 555-1234</p>
            </div>
            <img src="{imagen_escuela_url}" alt="School Picture">
        </div>
        <div class="contact-form">
            <h1>Formulario de Contacto</h1>
            <form action="/submit" method="post">
                <input type="text" name="nombre" placeholder="Tu nombre" required><br>
                <input type="email" name="email" placeholder="Tu email" required><br>
                <textarea name="mensaje" placeholder="Tu mensaje" rows="5" required></textarea><br>
                <button type="submit">Enviar</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)


