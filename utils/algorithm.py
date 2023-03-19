from models import Task


class Algorithm:
    def run(self, tasks: list[Task]) -> list[Task]:
        raise NotImplementedError()