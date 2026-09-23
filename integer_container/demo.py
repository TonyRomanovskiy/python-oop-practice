"""Demo of the IntegerContainerImpl."""

from integer_container import IntegerContainerImpl


def main():
    c = IntegerContainerImpl()

    print(c.add(5))       # 1
    print(c.add(10))      # 2
    print(c.add(1))       # 3
    print(c.get_median()) # 5

    c.add(4)              # [1, 4, 5, 10]
    print(c.get_median()) # 4

    print(c.delete(1))    # True
    print(c.get_median()) # 5


if __name__ == "__main__":
    main()