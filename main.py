from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/addi')
def int_addition():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result


@app.route('/subi')
def int_subtraction():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1-value2
    return '%d \n' % result



@app.route('/muli')
def int_multiplication():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1*value2
    return '%d \n' % result


@app.route('/divi')
def int_division():
    value1=request.args.get('A',default = 0, type = float)
    value2=request.args.get('B',default = 0, type = float)
    result=value1/value2
    return '%.2f \n' % result

@app.route('/addr')
def rat_addition():
    value1=request.args.get('A',default = 0, type = str)
    num1=str(value1).split('/')
    n1,d1=[int(x) for x in num1]
    value2=request.args.get('B',default = 0, type = str)
    num1=str(value2).split('/')
    n2,d2=[int(x) for x in num1]
    result=str(Fraction(n1,d1)+Fraction(n2,d2))
    return result


@app.route('/subr')
def rat_subtraction():
    value1=request.args.get('A',default = 0, type = str)
    num1=str(value1).split('/')
    n1,d1=[int(x) for x in num1]
    value2=request.args.get('B',default = 0, type = str)
    num1=str(value2).split('/')
    n2,d2=[int(x) for x in num1]
    result=str(Fraction(n1,d1)-Fraction(n2,d2))
    return result


@app.route('/mulr')
def rat_multiplication():
    value1=request.args.get('A',default = 0, type = str)
    num1=str(value1).split('/')
    n1,d1=[int(x) for x in num1]
    value2=request.args.get('B',default = 0, type = str)
    num1=str(value2).split('/')
    n2,d2=[int(x) for x in num1]
    result=str(Fraction(n1,d1)*Fraction(n2,d2))
    return result

@app.route('/divr')
def rat_division():
    value1=request.args.get('A',default = 0, type = str)
    num1=str(value1).split('/')
    n1,d1=[int(x) for x in num1]
    value2=request.args.get('B',default = 0, type = str)
    num1=str(value2).split('/')
    n2,d2=[int(x) for x in num1]
    result=str(Fraction(n1,d1)/Fraction(n2,d2))
    return result






if __name__ == "__main__":
    app.run()
