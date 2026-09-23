"""Demo of the logging system."""

from logger import ConsoleHandler, FileHandler, Logger


def main():
    logger = Logger([ConsoleHandler(), FileHandler()])

    # Через метод
    logger.log("Тестовое сообщение №1")

    # Через вызов объекта
    logger("Тестовое сообщение №2")

    # Несколько обработчиков одного типа
    logger2 = Logger([ConsoleHandler(), ConsoleHandler(), FileHandler()])
    logger2("Сообщение увидят два ConsoleHandler и один FileHandler")

    # Логгер без обработчиков
    empty_logger = Logger([])
    empty_logger("Это сообщение никуда не выведется")


if __name__ == "__main__":
    main()