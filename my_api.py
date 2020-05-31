#THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM AN API ENDPOINT
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#This is the data to manipulate
team = [{"id": "1", "name": "Thabo", "role": "Developer"}, {"id": "2", "name": "Thubelihle", "role": "Architect"}, 
    {"id": "3", "name": "Sello", "role": "Tutor"}, {"id": "4", "name": "Mavuso", "role": "SysOps"}]

#GET REQUEST
@app.route('/get', methods = ['GET'])
def getRequestHello():
    #return "Hi, I got your GET Request!"
    return jsonify({'result': 'Hello, this is a GET request!'}) 

#GET REQUEST
@app.route('/', methods = ['GET'])
def getNames():
    names = {}
    for name in team:
        names.update(name)
        print("Name : " + names["name"])
    return jsonify({"LIT Group": team})

#POST REQUEST
@app.route('/post', methods = ['POST'])
def postRequestHello():
    #return "I see you sent a POST message :-)"
    return jsonify({'result': 'I see you sent a POST message :-)'}) 

#UPDATE REQUEST
@app.route('/update', methods = ['PUT'])
def updateRequestHello():
    #return "Sending Hello on an PUT request!"
    return jsonify({'result': 'Sending Hello on an PUT request!'})

#DELETE REQUEST
@app.route('/delete', methods = ['DELETE'])
def deleteRequestHello():
    #return "Deleting your hard drive.....haha just kidding! I received a     DELETE request!"
    return jsonify({'result': "Deleting LIT Group... haha just kidding! I received a DELETE request!"})

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)  