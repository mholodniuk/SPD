from shared import Algorithm, Dataset, Scheduler, read_data_from_files


class SchrageAlgorithm(Algorithm):
    def run(self, dataset: Dataset) -> tuple[str, int]:
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


for tasks in read_data_from_files('./schrage/data'):
    scheduler = Scheduler(tasks)
    print(scheduler.run(SchrageAlgorithm()))
