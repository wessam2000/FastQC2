import os
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename
import urllib.request
from flask import Flask, request, redirect, jsonify
from GenertateUUID import generateUUID

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = "C:/Users/jihad abdelrazek/Desktop/python-flask-restful/UPLOAD_FOLDER"

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
# Actually setup the Api resource routing here
##
ALLOWED_EXTENSIONS = set(['fastq'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadAPI(Resource):
    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            # To use same file name => uncomment next line
            #filename = secure_filename(file.filename)
            filename, file_extension = os.path.splitext(file.filename)
            filename = secure_filename(generateUUID()+file_extension)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #call fastq function (os.path.join(app.config['UPLOAD_FOLDER']+filename)
            #["path/uuid.png","path/2.png"]
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify(
                {'message': 'Allowed file types are fastq'})
            resp.status_code = 400
            return resp


api.add_resource(UploadAPI, '/UploadAPI')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
