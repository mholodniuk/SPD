from shared import Algorithm, Dataset, read_data_from_files
from shared.algorithm import Scheduler


class SchrageAlgorithm(Algorithm):
    def run(self, dataset: Dataset) -> tuple[str, int]:
        tasks = dataset.tasks
        sorted_tasks = sorted(tasks, key=lambda t: t.release_time)
        ready_queue, schedule = [], []
        time, cmax = 0, 0
        
        while ready_queue or sorted_tasks:
            while sorted_tasks and sorted_tasks[0].release_time <= time:
                ready_queue.append(sorted_tasks.pop(0))
            
            if not ready_queue:
                time = sorted_tasks[0].release_time
                continue
            
            task = max(ready_queue, key=lambda t: t.delivery_time)
            ready_queue.remove(task)
            schedule.append(task)
            time += task.processing_time
            cmax = max(cmax, time + task.delivery_time)
        
        return (dataset.id, cmax)

for tasks in read_data_from_files('./schrage/data'):
    scheduler = Scheduler(tasks)
    print(scheduler.run(SchrageAlgorithm()))