from dataclasses import dataclass

@dataclass
class Task:
    release_time: int
    execution_time: int

@dataclass
class Dataset:
    id: str
    tasks: list[Task]