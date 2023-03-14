from dataclasses import dataclass

@dataclass
class Task:
    id: int
    available_time: int # release_time (?)
    execution_time: int

def sort_by_release_time(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda task: task.available_time)

def calculate_total_execution_time(tasks: list[Task]) -> int:
    sorted_tasks = sort_by_release_time(tasks)
    moments_of_task_termination = []
    for idx, task in enumerate(sorted_tasks):
        time = max((moments_of_task_termination[idx-1] if idx > 0 else 0, task.available_time)) + task.execution_time
        moments_of_task_termination.append(time)

    return moments_of_task_termination[-1]

task1 = Task(1, 2, 3)
task2 = Task(2, 3, 1)
task3 = Task(3, 8, 2)

print(calculate_total_execution_time(tasks=[task3, task2, task1]))