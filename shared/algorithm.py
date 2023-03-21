from abc import ABC, abstractmethod

from shared.models import Dataset


class Algorithm(ABC):
    @abstractmethod
    def run(self, tasks: Dataset) -> tuple[str, int]:
        pass


class Scheduler:
    def __init__(self, dataset: Dataset) -> None:
        self.dataset = dataset

    def run(self, algorithm: Algorithm):
        return algorithm.run(self.dataset)