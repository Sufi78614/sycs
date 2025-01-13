print("Name:Sufyan Ansari Roll:5008")
def count_ones_and_zeros(binary_string):
    count_ones = 0
    count_zeros = 0

    for char in binary_string:
        if char == '1':
            count_ones += 1
        elif char == '0':
            count_zeros += 1
        else:
            print(f"Invalid character '{char}' found in the string. Please enter a binary string.")
            return None

    return count_ones, count_zeros


def main():
    binary_string = input("Enter a binary string (composed of 0s and 1s): ")

    # Count the number of 1's and 0's
    result = count_ones_and_zeros(binary_string)

    if result is not None:
        count_ones, count_zeros = result
        print(f"Number of 1's: {count_ones}")
        print(f"Number of 0's: {count_zeros}")


if __name__ == "__main__":
    main()
