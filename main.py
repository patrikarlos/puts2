from flask import Flask, request
from fractions import Fraction
app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result

@app.route('/addr')
def rationaladdition():
    value1=request.args.get('A',default = 0, type = str)
    num1=str(value1).split('/')
    n1,d1=[int(x) for x in num1]
    value2=request.args.get('B',default = 0, type = str)
    num1=str(value2).split('/')
    n2,d2=[int(x) for x in num1]
    result=str(Fraction(n1,d1)+Fraction(n2,d2))
    return result


if __name__ == "__main__":
    app.run()
