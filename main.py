
from flask import Flask, request

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    d = request.args.get("X")

    l = d.split(",")

    f = []
    for i in l :

        if i.find('.') == -1 :
            i = int(i)
        else :
            i=  float(i)
        f.append(i)
    sum = 0

    for p in f :
        sum = sum + p

    return str(sum)


@app.route('/sub', methods=['GET'])
def sub():
    d = request.args.get("X")

    l = d.split(",")

    f = []
    if len(l) != 2 :
        return str("subtraction operation only be with 2 numbers")
    for i in l :

        if i.find('.') == -1 :
            i = int(i)
        else :
            i=  float(i)
        f.append(i)
    s = f[0]-f[1]

    return str(s)



@app.route('/mul', methods=['GET'])
def mul():
    d = request.args.get("X")

    l = d.split(",")

    f = []
    for i in l :

        if i.find('.') == -1 :
            i = int(i)
        else :
            i=  float(i)
        f.append(i)

    m = 1

    for p in f :
        m = m * p

    return str(m)




@app.route('/div', methods=['GET'])
def div():
    d = request.args.get("X")

    l = d.split(",")

    f = []
    if len(l) != 2 :
        return str("division operation only be with 2 numbers")
    for i in l :

        if i.find('.') == -1 :
            i = int(i)
        else :
            i=  float(i)
        f.append(i)
    s = f[0]/f[1]

    return str(s)



@app.route('/avg', methods=['GET'])
def avg():
    d = request.args.get("X")

    l = d.split(",")

    f = []
    for i in l :

        if i.find('.') == -1 :
            i = int(i)
        else :
            i=  float(i)
        f.append(i)
    s = 0

    for p in f :
        s = s + p
    a = s / len(f)
    return str(a)



if __name__ == '__main__':
    app.run(port = 5000 ,debug=True)
