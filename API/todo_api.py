from flask import Blueprint, request, jsonify

app_todo = Blueprint('todo', __name__)
tasks = []


@app_todo.route('/create',methods=['POST'])
def create_task():
    data=request.get_json()
    task=' '.join(data['tokens'][2:])
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'}), 201



@app_todo.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})


@app_todo.route('/tasks/<id>',methods=['GET'])
def get_task(id):
    if int(id)>=len(tasks)+1:
        return jsonify({'message': 'Task not found'}), 404
    else:
        return jsonify({'task':tasks[int(id)-1]})

@app_todo.route('/tasks/<id>',methods=['PUT'])
def put_task(id):
    if int(id)>=len(tasks)+1:
        return jsonify({'message': 'Task not found'}), 404
    else:
        data=request.get_json()
        task=' '.join(data['tokens'][6:])
        tasks[int(id)-1]=task
        return jsonify({'message': 'Task updated successfully'})

@app_todo.route('/tasks/<id>',methods=['DELETE'])
def delete_task(id):
    if int(id)>=len(tasks)+1:
        return jsonify({'message': 'Task not found'}), 404
    else:
        tasks.pop(int(id)-1)
        return jsonify({'message':'Task deleted successfully'})
            
