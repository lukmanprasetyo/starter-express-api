import flask
from flask import request
import numpy as np
import pickle

model = pickle.load(open('model/modelfp3.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    umur = int(request.form['umur'])
    fraksi_ejeksi = int(request.form['fraksi_ejeksi'])
    serum_creatinine = float(request.form['serum_creatinine'])
    anemia = float(request.form['anemia'])
    kreatin_fosfokinase = float(request.form['kreatin_fosfokinase'])
    diabetes = float(request.form['diabetes'])
    tekanan_darah_tinggi = float(request.form['tekanan_darah_tinggi'])
    platelets = float(request.form['platelets'])
    Sodium_kreatin = float(request.form['sodium_kreatin'])
    jenis_kelamin = float(request.form['jenis_kelamin'])
    perokok = float(request.form['perokok'])
    waktu = float(request.form['waktu'])
    predict_list = [[umur, fraksi_ejeksi, serum_creatinine, Sodium_kreatin, anemia, kreatin_fosfokinase, diabetes, tekanan_darah_tinggi, platelets, jenis_kelamin, waktu, perokok ]]
    prediction = model.predict(predict_list)
    output = {0: 'Tidak Meninggal', 1: 'Meninggal'}
    return flask.render_template('main.html', prediction_text='Prediksi Pasien Gagal Jantung yaitu {}'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)



 