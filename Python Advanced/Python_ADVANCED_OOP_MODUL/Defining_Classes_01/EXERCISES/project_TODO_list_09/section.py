from Python_ADVANCED_OOP_MODUL.Defining_Classes_01.EXERCISES.project_TODO_list_09.task import Task

"""
Pay attention to correct import path!!!!
"""

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if not new_task in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"
            

    def complete_task(self, task_name: str):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if filtered_tasks:
            task = filtered_tasks[0]
            task.completed = True
            return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"
    def clean_section(self):
        all_not_completed_tasks =[t for t in self.tasks if not t.completed]
        n_removed_tasks = len(self.tasks) - len(all_not_completed_tasks)
        self.tasks = all_not_completed_tasks
        return f"Cleared {n_removed_tasks} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for t in self.tasks:
            res += t.details() + "\n"
        return res

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
