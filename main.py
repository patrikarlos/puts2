from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<V1>&B=<V2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=v1+v2
    result= float(C)
    return '%d \n' % result


if __name__ == "__main__":
    app.run()
