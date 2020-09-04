from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}
]

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    id_todos = int(position) - 1
    del todos[id_todos]
    json_todos = jsonify(todos) 
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    body = json.loads(request_body)
    todos.append(body)
    json_todos = jsonify(todos) 
    print("Incoming request with the following body", request_body)
    return json_todos

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)   
    return json_todos



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)