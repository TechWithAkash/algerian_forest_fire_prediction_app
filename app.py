from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Landing page

@app.route('/predict')
def predict():
    return render_template('predict.html')  # Form page

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = scaler.transform([[Temperature, RH, WS, Rain, FFMC, DMC, ISI, Classes, Region]])
        prediction = ridge_model.predict(new_data_scaled)

        return render_template('prediction.html', prediction_text=f"The Fire Weather Index is: {prediction[0]:.2f}")

    except Exception as e:
        return render_template('prediction.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
