"""Demo of the TaskManagerImpl."""

from task_manager import TaskManagerImpl


def main():
    tm = TaskManagerImpl()

    print(tm.add_task("Купить хлеб", 3))                # 1
    print(tm.add_task("Сделать ДЗ", 5))                 # 2
    print(tm.add_task("Позвонить маме", 4))             # 3

    print(tm.list_tasks())
    print(tm.get_highest_priority_task())               # Сделать ДЗ

    tm.complete_task("Купить хлеб")
    print(tm.filter_completed_tasks())                  # ['Купить хлеб']

    tm.delete_task("Сделать ДЗ")
    print(tm.list_tasks())
    print(tm.get_highest_priority_task())               # Позвонить маме


if __name__ == "__main__":
    main()