import json


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos

    def get_web(self, id):
        return self.todos[id]

    def get_api(self, id):
        todo = [todo for todo in self.all() if todo['id'] == id]
        if todo:
            return todo[0]
        return []

    def create_web(self, data):
        data.pop('csrf_token')
        id_no = todos.all()[-1]['id'] + 1
        data['id'] = id_no
        self.todos.append(data)
        self.save_all()

    def create_api(self, data):
        self.todos.append(data)
        self.save_all()

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    def update_web(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    def update_api(self, id, data):
        todo = self.get(id)
        if todo:
            index = self.todos.index(todo)
            self.todos[index] = data
            self.save_all()
            return True
        return False

    def delete_web(self, id):
        self.todos.pop(id)
        self.save_all()

    def delete_api(self, id):
        todo = self.get(id)
        if todo:
            self.todos.remove(todo)
            self.save_all()
            return True
        return False


todos = Todos()
