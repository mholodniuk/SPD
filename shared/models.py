from dataclasses import dataclass

@dataclass
class Task:
    release_time: int
    processing_time: int
    delivery_time: int

@dataclass
class Dataset:
    id: str
    tasks: list[Task]