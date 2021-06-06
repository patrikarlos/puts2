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




if __name__ == '__main__':
    app.run(port = 5000 ,debug=True)
