from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('RandomForest.pkl')
scaler = joblib.load('df_escalado.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        whole_wt = float(request.form['whole_wt'])
        shucked_wt = float(request.form['shucked_wt'])
        shell_wt = float(request.form['shell_wt'])
        rings = float(request.form['rings'])
        
        input_data = pd.DataFrame({
            'length': [0],
            'diameter': [0],
            'height': [0],
            'whole_wt': [whole_wt],
            'shucked_wt': [shucked_wt],
            'viscera_wt': [0],
            'shell_wt': [shell_wt],
            'rings': [rings],
            'sex_F': [0],
            'sex_I': [0],
            'sex_M': [0],
        })

  # Escalar los datos de entrada
        scaled_data = scaler.transform(input_data)

        # Seleccionar solo las características usadas para el modelo
        scaled_data_for_prediction = scaled_data[:, [3,4,6,7]]  # Asegúrate de que estos índices son correctos

        # Realizar la predicción con los datos escalados
        prediccion = model.predict(scaled_data_for_prediction)

          # Devolver la predicción como JSON
        prediction_value = float(prediccion[0]) # Convertir a float si es necesario
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'resultado': prediction_value})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


