from flask import Flask, request
from sympy import Rational

app = Flask(__name__)

@app.route('/')
def index():
    return "Usage:curl -d 'A=val1&B=val2' -X POST http://localhost:5000/<oper>"


@app.route('/add',methods=['POST','GET'])
def addition():
    value1=Rational(request.form['A'])
    value2=Rational(request.form['B'])

    result=float(value1+value2)
    if result.is_integer():
        return str(int(result))+'\n'
    else:

        return str(result)+'\n'

@app.route('/sub',methods=['POST','GET'])
def subtraction():
    value1=Rational(request.form['A'])
    value2=Rational(request.form['B'])

    result=float(value1-value2)
    if result.is_integer():
        return str(int(result))+'\n'
    else:

        return str(result)+'\n'

@app.route('/mul',methods=['POST','GET'])
def multiplication():
    value1=Rational(request.form['A'])
    value2=Rational(request.form['B'])

    result=float(value1*value2)
    if result.is_integer():
        return str(int(result))+'\n'
    else:

        return str(result)+'\n'

@app.route('/div',methods=['POST','GET'])
def division():
    value1=Rational(request.form['A'])
    value2=Rational(request.form['B'])
    if value1 == 0 and value2 == 0:
        return "Undefined 0/0\n"
    elif value2==0 and value1<0:
        return "-oo\n"
    elif value2==0 and value1>0:
        return "oo\n"
        
    result=float(value1/value2)
    if result.is_integer():
        return str(int(result))+'\n'
    else:

        return str(result)+'\n'



if __name__ == "__main__":
    app.run()
