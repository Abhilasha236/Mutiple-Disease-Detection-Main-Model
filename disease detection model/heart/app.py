from flask import Flask, render_template, request, redirect, url_for
import pickle
import os

app = Flask(__name__)

# Load the model (ensure the path is correct)
model_path = os.path.join(os.getcwd(), 'heart/heart_disease_model.pkl')

# Ensure the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the trained model
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def heart_form():
    # Render the input form page (heart_page1.html)
    return render_template('heart_page1.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input data from the form with validation
        age = int(request.form['age'])
        sex = 0 if request.form['sex'] == 'male' else 1
        chest_pain = int(request.form['chestPain'])
        bp = int(request.form['trestbps'])
        cholesterol = int(request.form['cholesterol'])
        fbs_over_120 = 1 if request.form['fbsOver120'] == 'yes' else 0
        ekg_result = int(request.form['ekg'])
        max_hr = int(request.form['maxHr'])
        exercise_angina = 1 if request.form['exerciseAngina'] == 'yes' else 0
        st_depression = float(request.form['stDepression'])
        slope_of_st = int(request.form['slope'])
        num_vessels_fluro = int(request.form['ca'])
        thallium = int(request.form['thal'])

        # Create input data array for prediction
        input_data = [[
            age, sex, chest_pain, bp, cholesterol,
            fbs_over_120, ekg_result, max_hr, exercise_angina,
            st_depression, slope_of_st, num_vessels_fluro, thallium
        ]]

        # Make prediction
        prediction = model.predict(input_data)
        print(f"Prediction: {prediction[0]}")  # Debugging line
        result = "Positive for Heart Disease" if prediction[0] == 1 else "Negative for Heart Disease"

        # Render result page (heart_page2.html) and pass the result
        return render_template('heart_page2.html', result=result)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return redirect(url_for('heart_form'))  # Redirect back to form in case of error

# Route to display the doctors(GET request)
@app.route('/status')
def status():
    return "Heart App is Running!"

@app.route('/doctors')
def doctors():
    return render_template('doctor_details.html')

if __name__ == '__main__':
    # Start the Flask app in debug mode
    app.run(host="127.0.0.1", port=5001, threaded=True)
