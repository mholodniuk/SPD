from copy import deepcopy
from schrage import SchrageAlgorithm, SchragePMTNAlgorithm
from shared import Algorithm, Dataset, read_data_from_files
from shared.algorithm import Scheduler
from shared.models import Task
class CarlierAlgorithm(Algorithm):
    def run(self, dataset: Dataset) -> tuple[str, int]:
        ub = SchrageAlgorithm().run(dataset)[2]
        lb = SchragePMTNAlgorithm().run(dataset)[2]

        if lb == ub:
            return (dataset.id, ub)

        r_max_task = max(dataset.tasks, key=lambda task: task.release_time)
        q_min_task = min(dataset.tasks, key=lambda task: task.delivery_time)

        ct = SchrageAlgorithm().run(Dataset(dataset.id, 
                                            [r_max_task, q_min_task]))[2]

        q_min_task.processing_time = max(
            q_min_task.processing_time - (ct - q_min_task.release_time), 0)

        new_lb = SchragePMTNAlgorithm().run(dataset)[2]

        if new_lb < ub:
            ub = min(ub, self.run(dataset)[1])
        if new_lb < lb:
            lb = new_lb

        q_min_task.processing_time = min(q_min_task.processing_time + 
        (ct - q_min_task.release_time), q_min_task.processing_time)

        ct = SchrageAlgorithm().run(Dataset(dataset.id, 
                    [r_max_task, q_min_task]))[2]
        
        new_ub = ct + q_min_task.delivery_time + \
        SchrageAlgorithm().run(Dataset(dataset.id, 
                                [q_min_task, r_max_task]))[2]

        if new_ub < ub:
            ub = new_ub
        if new_ub < lb:
            lb = min(lb, self.run(Dataset(dataset.id, 
                                [q_min_task, r_max_task]))[1])

        return (dataset.id, lb)
    

if __name__ == '__main__':
    for tasks in read_data_from_files('./carlier/data'):
        scheduler = Scheduler(tasks)
        scheduler.run(CarlierAlgorithm())
