from flask import Flask, request
from sympy import Rational

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


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

    result=float(value1/value2)
    if result.is_integer():
        return str(int(result))+'\n'
    else:

        return str(result)+'\n'



if __name__ == "__main__":
    app.run()
