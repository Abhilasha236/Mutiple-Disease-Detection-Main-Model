from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)

# Global variables for the model and scaler
model = None
scaler = None

# Dictionary for encoding categorical inputs
dictionary = {
    "rbc": {"abnormal": 1, "normal": 0},
    "pc": {"abnormal": 1, "normal": 0},
    "pcc": {"present": 1, "notpresent": 0},
    "ba": {"notpresent": 0, "present": 1},
    "htn": {"yes": 1, "no": 0},
    "dm": {"yes": 1, "no": 0},
    "cad": {"yes": 1, "no": 0},
    "appet": {"good": 1, "poor": 0},
    "pe": {"yes": 1, "no": 0},
    "ane": {"yes": 1, "no": 0},
}

# Load the model and scaler when the application starts
def load_resources():
    global model, scaler
    try:
        # Load the model
        model_path = os.path.join(os.getcwd(), 'kidney/kidney_disease_prediction.pkl')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
            print("Model loaded successfully!")

        # Load the scaler
        scaler_path = os.path.join(os.getcwd(), 'kidney\\scaler.pkl')
        if not os.path.exists(scaler_path):
            raise FileNotFoundError(f"Scaler file not found at {scaler_path}")
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
            print("Scaler loaded successfully!")

    except Exception as e:
        print(f"Error loading resources: {str(e)}")
        model = None
        scaler = None

# Call this function to load the resources
load_resources()

# Function to make a prediction based on the input data
def predict_kidney_disease(age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, wc, htn, dm, cad, pe, ane, pot):
    try:
        if model is None or scaler is None:
            return "Error: Model or Scaler not loaded!"

        # Use dictionary to map categorical values to binary values
        rbc_encoded = dictionary["rbc"].get(rbc, -1)
        pc_encoded = dictionary["pc"].get(pc, -1)
        pcc_encoded = dictionary["pcc"].get(pcc, -1)
        ba_encoded = dictionary["ba"].get(ba, -1)
        htn_encoded = dictionary["htn"].get(htn, -1)
        dm_encoded = dictionary["dm"].get(dm, -1)
        cad_encoded = dictionary["cad"].get(cad, -1)
        pe_encoded = dictionary["pe"].get(pe, -1)
        ane_encoded = dictionary["ane"].get(ane, -1)

        # Check for invalid inputs
        if -1 in [rbc_encoded, pc_encoded, pcc_encoded, ba_encoded, htn_encoded, dm_encoded, cad_encoded, pe_encoded, ane_encoded]:
            return "Error: Invalid categorical input!"

        # Prepare the input data in the same format as the training data
        input_data = [
            [age, bp, al, su, bgr, bu, sc, wc, pot] +
            [rbc_encoded, pc_encoded, pcc_encoded, ba_encoded, htn_encoded, dm_encoded, cad_encoded, pe_encoded, ane_encoded]
        ]

        # Scale the input data
        scaled_input_data = scaler.transform(input_data)

        # Predict using the trained model
        prediction = model.predict(scaled_input_data)

        # Return a meaningful prediction result
        return "Kidney Disease Present" if prediction[0] == 1 else "Kidney Disease Absent"

    except Exception as e:
        return f"Error in prediction: {str(e)}"

# Home route to serve the HTML page
@app.route('/')
def home():
    return render_template('kidney_p1.html')  # Main HTML page for input

# API route to handle prediction (POST request)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Validate required fields
        required_fields = ['age', 'bp', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc', 'wc', 'htn', 'dm', 'cad', 'pe', 'ane', 'pot']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Extract values
        age = float(data['age'])
        bp = float(data['bp'])
        al = float(data['al'])
        su = float(data['su'])
        rbc = data['rbc']
        pc = data['pc']
        pcc = data['pcc']
        ba = data['ba']
        bgr = float(data['bgr'])
        bu = float(data['bu'])
        sc = float(data['sc'])
        wc = float(data['wc'])
        htn = data['htn']
        dm = data['dm']
        cad = data['cad']
        pe = data['pe']
        ane = data['ane']
        pot = float(data['pot'])

        # Call the prediction function
        prediction = predict_kidney_disease(
            age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, wc, htn, dm, cad, pe, ane, pot
        )

        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

# Route to display the result (GET request)
@app.route('/result')
def result():
    prediction = request.args.get('prediction')  # Get prediction from query parameter
    return render_template('kidney_p2.html', prediction=prediction)  # Result HTML page

# Route to display doctor details (GET request)
@app.route('/doctors')
def doctors():
    return render_template('doctor_details.html')  # Doctor details HTML page

# Main function to run the app
if __name__ == '__main__':
    app.run(port=5003, threaded=True)
