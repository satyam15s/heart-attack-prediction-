# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load the Random Forest CLassifier model
filename = 'heart.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form.get('sex')

      
        
        cp = request.form.get('cp')
        trtbps = int(request.form['trtbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalachh = int(request.form['thalachh'])
        exng = request.form.get('exng')
       
        caa = int(request.form['caa'])
        
        
        data = np.array([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,caa]])
        data = np.nan_to_num(data)
        
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)
