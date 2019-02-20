from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add',methods=['POST','GET'])
def addition():
    value1=int(request.form['A'])
    value2=int(request.form['B'])
    result=value1+value2
    return '%d \n' % result

@app.route('/sub',methods=['POST','GET'])
def subtraction():
    value1=int(request.form['A'])
    value2=int(request.form['B'])
    result=value1-value2
    return '%d \n' % result

@app.route('/mul',methods=['POST','GET'])
def multiplication():
    value1=int(request.form['A'])
    value2=int(request.form['B'])
    result=value1*value2
    return '%d \n' % result

@app.route('/div',methods=['POST','GET'])
def division():
    value1=int(request.form['A'])
    value2=int(request.form['B'])
    result=value1/value2
    return '%d \n' % result




if __name__ == "__main__":
    app.run()
