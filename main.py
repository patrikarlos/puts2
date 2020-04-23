from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
    return 'write values of A and B'
	#return 'write in the format of url/operation? A=value & B=value'
@app.route('/add')
def addition():
    try:
        arg1 = request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError:
        arg1 = 'None'
    try:
        arg2 = request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError:
        arg2 = 'None'
    if arg1=='None' or arg2 == 'None':
        return'None'
    else:
        X= Fraction(arg1)
        Y = Fraction(arg2)
        Z = X+Y
        return str(round(float(Z),3))
if __name__ == "__main__":
    app.run(debug=True)
