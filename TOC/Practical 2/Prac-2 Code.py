Q.design a program for creating that machine accept three consecutive 1s

def is_divisible_by_2(number_str):
    
    if not number_str.isdigit():
        print("Invalid input! Please enter a valid decimal number.")
        return False

    last_digit = number_str[-1]

    # Check if the last digit is even (0, 2, 4, 6, 8)
    if last_digit in '02468':
        return True
    else:
        return False


def main():
    number_str = input("Enter a decimal number: ").strip()

    if is_divisible_by_2(number_str):
        print(f"The number {number_str} is divisible by 2.")
    else:
        print(f"The number {number_str} is not divisible by 2.")


if __name__ == "__main__":
    main()
