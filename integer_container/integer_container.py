"""Integer container with add, delete and median operations."""

from abc import ABC


class IntegerContainer(ABC):
    """Abstract integer container interface."""

    def add(self, value: int) -> int:
        """Add value and return the number of elements after addition."""
        return 0

    def delete(self, value: int) -> bool:
        """Remove value if present. Return True on success."""
        return False

    def get_median(self) -> int | None:
        """Return median or None if empty. For even — leftmost of two middle."""
        return None


class IntegerContainerImpl(IntegerContainer):
    """Concrete integer container."""

    def __init__(self):
        self.container = []

    def add(self, value: int) -> int:
        self.container.append(value)
        return len(self.container)

    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False

    def get_median(self) -> int | None:
        if not self.container:
            return None

        self.container.sort()
        length = len(self.container)
        if length % 2 == 0:
            return self.container[length // 2 - 1]
        return self.container[length // 2]