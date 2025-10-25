from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form['name']
    age = int(request.form['age'])
    heart_rate = int(request.form['heart_rate'])
    temperature = float(request.form['temperature'])
    spo2 = int(request.form['spo2'])

    status = "Normal"

    # Simple analysis logic
    if temperature > 37.5 or heart_rate > 100 or spo2 < 95:
        status = "Warning"
    if temperature > 39 or heart_rate > 120 or spo2 < 90:
        status = "Critical"

    return render_template('result.html',
                           name=name,
                           age=age,
                           heart_rate=heart_rate,
                           temperature=temperature,
                           spo2=spo2,
                           status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
