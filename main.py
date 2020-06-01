from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
    Value1=request.args.get('A',default = 0, type = Fraction)
    Value2=request.args.get('B',default = 0, type = Fraction)
    data=Value1+Value2
    result= float(data)
    return '%d \n' % result


if __name__ == "__main__":
    app.run()
