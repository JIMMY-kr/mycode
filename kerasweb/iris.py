from flask import  Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

@app.route('/iris', methods=['GET'])
def main():
    return render_template('iris/input.html')

@app.route('/iris_result', methods=['POST'])
def iris_result():
    flowers = ['setosa', 'versicolor', 'virginica']
    # 기계학습 모형이 저장된 디렉토리
    model = load_model('c:/data/iris/iris_keras.model')

    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    test_set = np.array([[a,b,c,d]])
    pred=model.predict(test_set)
    n=np.argmax(pred,axis=1)
    result = flowers[n[0]]
    return render_template('iris/result.html',
                            result=result, a=a, b=b, c=c, d=d)

if __name__ == '__main__':
    app.run(port=8000, threaded=False)
