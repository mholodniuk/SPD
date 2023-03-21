from pathlib import Path

from shared.models import Dataset, Task


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
