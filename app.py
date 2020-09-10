from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from flask_cors import cross_origin, CORS
import gunicorn

app = Flask(__name__)
model = pickle.load(open('diabetes.pkl', 'rb'))
app.secret_key = '123'


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    Pregnancies = request.form['Pregnancies']
    Glucose = request.form['Glucose']
    BloodPressure = request.form['BloodPressure']
    SkinThickness = request.form['SkinThickness']
    Insulin = request.form['Insulin']
    BMI = request.form['BMI']
    DPF = request.form['DPF']
    Age = request.form['Age']
    final = [[int(Pregnancies), int(Glucose), int(BloodPressure), int(SkinThickness), int(Insulin), float(BMI), float(DPF),
             int(Age)]]
    prediction = model.predict(final)
    final_pred = int(prediction[0])
    if final_pred == 0:
        output = 'Most likely you are not diabetic'
    else:
        output = 'Most likely you are diabetic'

    session['output'] = output

    return redirect(url_for('result'))


@app.route('/result', methods=['GET'])
@cross_origin()
def result():
    out = session.pop('output')
    return render_template('result.html', prediction_text=out)


if __name__ == '__main__':
    app.run(debug=True)
