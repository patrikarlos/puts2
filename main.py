from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    data=value1+value2
    result= float(data)
    return '%d \n' % result

@app.route('/sub')
def subtraction():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    data=value1-value2
    result= float(data)
    return '%d \n' % result

@app.route('/multiplication')
def multiplication():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    data=value1*value2
    result= float(data)
    return '%d \n' % result



if __name__ == "__main__":
    app.run()
