from flask import Flask, request

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

if __name__ == '__main__':
    app.run(port = 5000 ,debug=True)
