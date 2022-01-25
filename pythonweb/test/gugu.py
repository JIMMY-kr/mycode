from flask import Flask, Markup, render_template, request
#앱 생성
app = Flask(__name__)

#url pattern
@app.route('/',methods=['GET'])
def main():
    return render_template('gugu.html') #template을 실행 >>> html 생성

@app.route('/gugu_result', methods=['POST'])
def gugu_result():
    dan = int(request.form['dan'])
    result=''
    for i in range(1, 10):
        result += f'{dan}x{i}={dan*i}<br>'
    result = Markup(result)
    return render_template('gugu_result.html',
                               result=result)


if __name__ == '__main__':
    app.run(port=8000, threaded=False)