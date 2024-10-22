from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_command1', methods=['POST'])
def run_command1():
    # Example: Run "ls" command or another function
    command = "aplay audio/abhimaja.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command2', methods=['POST'])
def run_command2():
    # Example: Run "uname -a" or another command
    command = "aplay audio/baburao.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command3', methods=['POST'])
def run_command3():
    command = "aplay audio/bai_kayprakar.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command4', methods=['POST'])
def run_command4():
    command = "aplay audio/golmal.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command5', methods=['POST'])
def run_command5():
    command = "aplay audio/hey_prabhu.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command6', methods=['POST'])
def run_command6():
    command = "aplay audio/kehna_kya.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command7', methods=['POST'])
def run_command7():
    command = "aplay audio/khatam.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command8', methods=['POST'])
def run_command8():
    command = "aplay audio/laugh.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command9', methods=['POST'])
def run_command9():
    command = "aplay audio/pagal.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command10', methods=['POST'])
def run_command10():
    command = "aplay audio/rukojara.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command11', methods=['POST'])
def run_command11():
    command = "aplay audio/so_beatiful.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command12', methods=['POST'])
def run_command12():
    command = "aplay audio/sunai.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command13', methods=['POST'])
def run_command13():
    command = "aplay audio/bai_kayprakar.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

@app.route('/run_command14', methods=['POST'])
def run_command14():
    command = "aplay audio/bai_kayprakar.wav"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return render_template('index.html', output=result.stdout)

#@app.route('/run_command3', methods=['POST'])
#def run_command3():
    # Example: Run "df -h" or another command
#    command = "df -h"
#    result = subprocess.run(command, shell=True, capture_output=True, text=True)
#    return render_template('index.html', output=result.stdout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)