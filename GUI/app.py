from flask import Flask, render_template, redirect, url_for
import subprocess
import threading
import os

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for Menu Page
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Route to Launch Streamlit App
@app.route('/predict')
def predict():
    # Start Streamlit in a separate thread if not already running
    if not os.environ.get("STREAMLIT_RUNNING"):
        threading.Thread(target=run_streamlit, daemon=True).start()
        os.environ["STREAMLIT_RUNNING"] = "1"
    
    # Redirect to the Streamlit app URL in the same tab
    return redirect("http://127.0.0.1:8501", code=302)

def run_streamlit():
    # Run the Streamlit app using subprocess
    subprocess.Popen(["streamlit", "run", "view.py"])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # Prevents Flask from restarting twice