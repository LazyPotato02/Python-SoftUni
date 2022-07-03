from .task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        else:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str) -> str:
        task = None
        for t in self.tasks:
            if t.name == task_name:
                task = t
                break

        if task:
            task.completed = True
            return f'Completed task {task_name}'
        else:
            return f'Could not find task with the name {task_name}'

    def clean_section(self) -> str:
        i = 0
        for task in [t for t in self.tasks if t.completed is True]:
            self.tasks.pop(self.tasks.index(task))
            i += 1
        return f'Cleared {i} tasks.'

    def view_section(self) -> str:
        retval = f"Section {self.name}:"
        if self.tasks:
            retval += '\n' + '\n'.join([task.details() for task in self.tasks])
        return retval