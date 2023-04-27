from abc import ABC, abstractmethod

from shared.models import Dataset, Task


class Algorithm(ABC):
    @abstractmethod
    def run(self, tasks: Dataset) -> tuple[str, list[Task], int]:
        pass


class Scheduler:
    def __init__(self, dataset: Dataset) -> None:
        self.dataset = dataset

    def run(self, algorithm: Algorithm) -> None:
        result = algorithm.run(self.dataset)
        print(result)
