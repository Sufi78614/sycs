class ListADT:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError("Item not found in list")

    def size(self):
        return len(self.items)

    def contains(self, item):
        return item in self.items

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("Index out of bounds")

if __name__ == "__main__":
    lst = ListADT()

    print("Is the list empty?", lst.is_empty())

    lst.add(1)
    lst.add(2)
    lst.add(3)

    print("List size:", lst.size())
    print("List contains 2?", lst.contains(2))

    print("\nList elements:")
    for i in range(lst.size()):
        print(lst.get(i))

    lst.remove(2)
    print("\nList elements after removing 2:")
    for i in range(lst.size()):
        print(lst.get(i))
