#!flask/bin/python
from flask import Flask
from flask import jsonify, request, make_response
import uuid

app = Flask(__name__)

db = {'22b646b2-7806-43d8-956d-702ccd9af7b8':
        {
            'id': '22b646b2-7806-43d8-956d-702ccd9af7b8',
            'title': 'Setup Kong API gateway', 
            'description': 'Setup Kong API gateway for PropertyGuru on each env.',
        },
    }

@app.route('/ping')
def index():
    return 'pong'

@app.route('/v1/todos', methods=['GET'])
def list_todos():
    todos = []
    for key, value in db.items():
        todos.append(value)

    return jsonify(todos)

@app.route('/v1/todos/<string:id>', methods=['GET'])
def get_todo(id):
    if id not in db:
        return make_response(jsonify({'error': 'id ' + id + ' is not found'}), 404)

    todo = db[id]
    response = jsonify(todo)
    response.add_etag()

    return response

@app.route('/v1/todos/<string:id>', methods=['PUT'])
def update_todo(id):
    if id not in db:
        return make_response(jsonify({'error': 'id ' + id + ' is not found'}), 404)

    todo = request.json
    todo['id'] = id
    db[id] = todo

    return make_response(jsonify(todo), 200)

@app.route('/v1/todos', methods=['POST'])
def create_todo():
    todo = request.json
    id = str(uuid.uuid4())
    todo['id'] = id
    db['id'] = todo
    
    return make_response(jsonify(todo), 201)

@app.route('/v1/todos/<string:id>', methods=['DELETE'])
def delete_todo(id):
    if id not in db:
        return make_response(jsonify({'error': 'id ' + id + ' is not found'}), 404)

    del db[id]

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
