from flask import Flask, render_template, redirect, url_for
import subprocess  # Use subprocess for non-blocking process execution
import sys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heart')
def heart():
    print("Redirecting to heart app...")
    python_path = sys.executable
    subprocess.Popen([python_path, 'heart/app.py'])
    return redirect("http://127.0.0.1:5001")

@app.route('/liver')
def liver():
    print("Redirecting to liver app...")
    
    # Run the liver app in a separate process without blocking the main app
    subprocess.Popen(['python', 'liver/app.py'])
    
    # Redirect to the liver app which runs on port 5002
    return redirect("http://127.0.0.1:5002")

@app.route('/kidney')
def kidney():
    print("Redirecting to kidney app...")
    python_path = sys.executable
    subprocess.Popen([python_path, 'kidney/app.py'])
    return redirect("http://127.0.0.1:5003")

if __name__ == "__main__":
    app.run(port=5000)
