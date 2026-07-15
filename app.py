from flask import Flask, render_template, url_for 
import subprocess

app = Flask(__name__)
process = None #changw

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/start',methods=['POST'])
def start():
    global process#chnage
    if process is None or process.poll() is not None:#change
        process = subprocess.Popen(["python", "eyes_mouse.py"])#change
        return "started"#change
    subprocess.Popen(["python", "eyes_mouse.py"])
    return (url_for('dashboard'))
@app.route('/stop', methods=['POST'])
def stop():
    global process
    if process is not None and process.poll() is None:
        process.terminate()
        process = None
        return "stopped"
    return "not running"
if __name__ == "__main__":
    app.run(debug=True)