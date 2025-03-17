class ArrayADT:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity  # Initialize array with None values

    def get(self, index):
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.capacity:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def size(self):
        return self.capacity

# Example usage:
if __name__ == "__main__":
    array_adt = ArrayADT(5)  # Create an array ADT of capacity 5

    print("Array capacity:", array_adt.size())

    # Set values in the array
    array_adt.set(0, 1)
    array_adt.set(1, 3)
    array_adt.set(2, 5)
    array_adt.set(3, 7)
    array_adt.set(4, 9)

    # Get values from the array and print
    print("\nArray elements:")
    for i in range(array_adt.size()):
        print(array_adt.get(i))
