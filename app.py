from flask import Flask, render_template, url_for 
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/start')
def start():
    subprocess.Popen(["python", "eyes_mouse.py"])
    return (url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)