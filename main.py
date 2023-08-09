from flask import Flask,jsonify,render_template,request
import numpy as np
import pickle
app=Flask(__name__)

modelo=pickle.load(open('static/modelo.pkl','rb'))
@app.route('/')
def method_name():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        float_features=[float(x) for x in request.form.values()]
        features=[np.array(float_features)]
        prediction=modelo.predict(features)
        return render_template('index.html', result=f'a flor diagnosticada e: {prediction[0]}')
        
if __name__=='__main__':
    app.run()
