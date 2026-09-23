"""Logging system with handlers and timestamp formatting."""

from abc import ABC, abstractmethod
from datetime import datetime


class Handler(ABC):
    """Abstract handler interface."""

    @abstractmethod
    def emit(self, message: str):
        """Send a message somewhere (console, file, etc.)."""
        pass


class ConsoleHandler(Handler):
    """Handler that prints messages to console."""

    def emit(self, message: str) -> None:
        print(message)


class FileHandler(Handler):
    """Handler that returns a formatted string for file writing."""

    def emit(self, message: str) -> str:
        return f"Запись в файл: {message}"


class TimeMixin:
    """Mixin that adds timestamp formatting."""

    def format_with_timestamp(self, message: str) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{timestamp}] [{message}]"


class Logger(TimeMixin):
    """Logger that sends formatted messages to all handlers."""

    def __init__(self, handlers: list):
        self._handlers = handlers

    def log(self, message: str) -> None:
        """Format the message with timestamp and emit to all handlers."""
        formatted = self.format_with_timestamp(message)
        for handler in self._handlers:
            handler.emit(formatted)

    def __call__(self, message: str) -> None:
        self.log(message)