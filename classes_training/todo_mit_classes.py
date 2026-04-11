# Refactor Todo-List-App with Classes

class TodoList:
    def __init__(self):
        # Wie speicherst du die Todos?
        pass

    def add(self, task):
        pass

    def show(self):
        pass

    def complete(self, index):
        pass

    def delete(self, index):
        pass


# Hauptprogramm – soll genauso funktionieren wie oben:
my_list = TodoList()
my_list.add("Python lernen")
my_list.add("Trompete üben")
my_list.show()
my_list.complete(1)
my_list.show()
my_list.delete(2)
my_list.show()
