from dataclasses import dataclass

@dataclass
class Task:
    id: int
    release_time: int
    execution_time: int

def sort_by_release_time(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda task: task.release_time)

def calculate_total_execution_time(tasks: list[Task]) -> int:
    sorted_tasks = sort_by_release_time(tasks)
    moments_of_task_termination = []
    for idx, task in enumerate(sorted_tasks):
        time = max((moments_of_task_termination[idx-1] if idx > 0 else 0, task.release_time)) + task.execution_time
        moments_of_task_termination.append(time)

    return moments_of_task_termination[-1]

# todo: cos zeby wczytywac dane z plikow

task1 = Task(1, 1, 5)
task2 = Task(2, 4, 5)
task3 = Task(3, 1, 4)
task4 = Task(4, 7, 3)
task5 = Task(5, 3, 6)
task6 = Task(6, 4, 7)

tasks = [task1, task2, task3, task4, task5, task6]

print(calculate_total_execution_time(tasks))