import math
from shared import Algorithm, Dataset, read_data_from_files
from shared.algorithm import Scheduler
from shared.models import Task


class SchrageAlgorithm(Algorithm):
    def run(self, dataset: Dataset) -> tuple[str, list[Task], int]:
        tasks = dataset.tasks
        sorted_tasks = sorted(tasks, key=lambda t: t.release_time)
        ready_queue, scheduled = [], []
        time, cmax = 0, 0

        while ready_queue or sorted_tasks:
            while sorted_tasks and sorted_tasks[0].release_time <= time:
                ready_queue.append(sorted_tasks.pop(0))

            if not ready_queue:
                time = sorted_tasks[0].release_time
                continue

            task = max(ready_queue, key=lambda t: t.delivery_time)
            ready_queue.remove(task)
            scheduled.append(task)
            time += task.processing_time
            cmax = max(cmax, time + task.delivery_time)

        return (dataset.id, scheduled, cmax)


class SchragePMTNAlgorithm(Algorithm):
    def run(self, dataset: Dataset) -> tuple[str, list[Task], int]:
        tasks = dataset.tasks
        ready, scheduled = [], []
        not_ready = [task for task in tasks]
        current_time, cmax = 0, 0
        l = Task(0, 0, math.inf)
        while ready or not_ready:
            while not_ready and min(not_ready, key=lambda task: task.release_time).release_time <= current_time:
                task = min(not_ready, key=lambda task: task.release_time)
                not_ready.remove(task)
                ready.append(task)
                if task.delivery_time > l.delivery_time:
                    l.processing_time = current_time - task.release_time
                    current_time = task.release_time
                    if l.processing_time > 0:
                        ready.append(l)
                    l = task

            if not ready:
                current_time = min(
                    not_ready, key=lambda task: task.release_time).release_time
            else:
                task = max(ready, key=lambda task: task.delivery_time)
                ready.remove(task)
                scheduled.append(task)
                l = task
                current_time += task.processing_time
                cmax = max(cmax, current_time + task.delivery_time)
        return (dataset.id, scheduled, cmax)


if __name__ == '__main__':
    print('bez podziału')
    for tasks in read_data_from_files('./schrage/data'):
        scheduler = Scheduler(tasks)
        scheduler.run(SchrageAlgorithm())

    print('\n=====================\n')

    print('z podziałem')
    for tasks in read_data_from_files('./schrage/data'):
        scheduler = Scheduler(tasks)
        scheduler.run(SchragePMTNAlgorithm())
