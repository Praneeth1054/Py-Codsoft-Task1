import json

class ToDoList:
    def __init__(self):  # Corrected __init__ method
        self.tasks = []

    def add_task(self, task, priority):
        self.tasks.append({"task": task, "priority": priority, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} (Priority: {task['priority']}) - {status}")

    def mark_complete(self, task_no):
        if 0 < task_no <= len(self.tasks):
            self.tasks[task_no - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
        print("Tasks saved successfully.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")

# Example Usage
todo = ToDoList()
todo.add_task("Complete Python project", "High")
todo.add_task("Go for a walk", "Medium")
todo.view_tasks()
todo.mark_complete(1)
todo.view_tasks()
todo.save_tasks()
todo.load_tasks()
