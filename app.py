from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('randomForestestetica.pkl')
scaler = joblib.load('scalerestetica.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        citas_canceladas= float(request.form['citas_canceladas']);
        citas_totales = (request.form['citas_totales']);
        hora =(request.form['hora']);
        dia =(request.form['dia']);

        data = pd.DataFrame({
            'servicio': [0],
            'precio': [0],
            'duracion': [0],
            'dia': [dia],
            'mes': [0],
            'hora': [hora],
            'citas_totales': [citas_totales],
            'citas_canceladas': [citas_canceladas],
        })


        scaled_data = scaler.transform(data)
        scaled_data_for_prediction = scaled_data[:, [-1,-2,-3,-5]]

        prediccion = model.predict(scaled_data_for_prediction)

        resultado = (prediccion[0])

        return ({'prediction': resultado})
     
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


