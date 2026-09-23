"""Task manager with priorities and completion status."""

from abc import ABC, abstractmethod


class TaskManager(ABC):
    """Abstract task manager interface."""

    @abstractmethod
    def add_task(self, task: str, priority: int = 0) -> int:
        """Add a task. Return the number of tasks after addition."""
        pass

    @abstractmethod
    def delete_task(self, task: str) -> bool:
        """Delete a task. Return True on success."""
        pass

    @abstractmethod
    def list_tasks(self) -> list:
        """Return all task names."""
        pass

    @abstractmethod
    def get_highest_priority_task(self) -> str | None:
        """Return the task with the highest priority, or None if empty."""
        pass

    @abstractmethod
    def complete_task(self, task: str) -> bool:
        """Mark a task as completed. Return True on success."""
        pass

    @abstractmethod
    def filter_completed_tasks(self) -> list:
        """Return list of completed task names."""
        pass


class TaskManagerImpl(TaskManager):
    """Concrete task manager using dict for storage."""

    def __init__(self):
        self._tasks = {}

    def add_task(self, task: str, priority: int = 0) -> int:
        if task not in self._tasks:
            self._tasks[task] = {"priority": priority, "completed": False}
        return len(self._tasks)

    def delete_task(self, task: str) -> bool:
        if task in self._tasks:
            del self._tasks[task]
            return True
        return False

    def list_tasks(self) -> list:
        return list(self._tasks.keys())

    def get_highest_priority_task(self) -> str | None:
        return max(
            self._tasks,
            key=lambda t: self._tasks[t]["priority"],
            default=None,
        )

    def complete_task(self, task: str) -> bool:
        if task in self._tasks:
            self._tasks[task]["completed"] = True
            return True
        return False

    def filter_completed_tasks(self) -> list:
        return [
            task for task, data in self._tasks.items()
            if data["completed"]
        ]