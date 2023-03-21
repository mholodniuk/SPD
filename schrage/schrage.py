from dataclasses import dataclass
from pathlib import Path
import numpy as np


@dataclass
class Task:
    release_time: int
    processing_time: int
    delivery_time: int


@dataclass
class Dataset:
    id: str
    tasks: list[Task]


def schrage(dataset: Dataset) -> int:
    tasks = dataset.tasks
    ready_queue = list()
    task_list = sorted(tasks, key=lambda x: x.release_time)
    current_time, Cmax = task_list[0].release_time, 0

    while ready_queue or task_list:
        while task_list and task_list[0].release_time <= current_time:
            ready_queue.append(task_list.pop(0))

        if not ready_queue:
            current_time = task_list[0].release_time
        else:
            task = max(ready_queue, key=lambda task: task.delivery_time)
            ready_queue.remove(task)
            current_time += task.processing_time
            Cmax = max(Cmax, current_time + task.delivery_time)

    return (dataset.id, Cmax)


def read_data_from_files(path_str: str) -> list[Dataset]:
    files = [item.absolute() for item in Path(path_str).iterdir() if item.is_file()]
    data = []
    for file in files:
        with file.open() as f:
            current_file_data = []
            for line in f:
                if len(line.split()) != 3:
                    continue
                nums = line.split()
                current_file_data.append(
                    (int(nums[0]), int(nums[1]), int(nums[2])))
        data.append(
            Dataset(file.name, create_tasks_from_tuple_list(current_file_data)))

    return data


def create_tasks_from_tuple_list(task_list: list[tuple[int, int, int]]) -> list[Task]:
    return [Task(raw_task_data[0], raw_task_data[1], raw_task_data[2]) for raw_task_data in task_list]


for tasks in read_data_from_files('./data'):
    print(schrage(tasks))
