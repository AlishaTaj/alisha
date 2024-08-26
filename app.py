# app.py
from flask import Flask, render_template, request
from cloud import predict_weight

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_weight = None
    if request.method == 'POST':
        height_value = float(request.form['height'])
        predicted_weight = predict_weight(height_value)
    return render_template('index.html', predicted_weight=predicted_weight)

if __name__ == '__main__':
    app.run(debug=True)
