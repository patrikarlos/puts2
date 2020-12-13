from flask import Flask, request
import statistics

app = Flask(__name__)


@app.route('/average', methods=['GET'])
def average():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    for n in vector :
        sum = sum + n
    avg = sum / len(vector)
    return str(avg)

@app.route('/mean', methods=['GET'])
def mean():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    for n in vector :
        sum = sum + n
    avg = sum / len(vector)
    return str(avg)

@app.route('/avg', methods=['GET'])
def avg():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    for n in vector :
        sum = sum + n
    avg = sum / len(vector)
    return str(avg)

@app.route('/median', methods=['GET'])
def median():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    med = statistics.median(vector)
    return str(med)

@app.route('/maximum', methods=['GET'])
def maximum():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    m = max(vector)
    return str(m)

@app.route('/minimum', methods=['GET'])
def minimum():
    data = request.args.to_dict()
    print(data)
    string = data['X']
    vector = string.split(",")
    sum = 0
    for i in range(len(vector)) :
        if vector[i].find('.') == -1 :
            vector[i] = int(vector[i])
        else :
            vector[i]= float(vector[i])

    print(vector)
    m = min(vector)
    return str(m)




if __name__ == '__main__':
    app.run(port = 5000 ,debug=True)
