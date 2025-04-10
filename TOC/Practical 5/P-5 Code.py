Q. design a program for creating a machine which accept string having equal number of 1s and 0s
print("Name:Sufyan Ansari Roll:5008")
def has_equal_ones_and_zeros(s):
    
    count_ones = s.count('1')
    count_zeros = s.count('0')
    
    return count_ones == count_zeros

def main():
    user_input = input("Enter a string containing only '0's and '1's: ")
    
    if not all(char in '01' for char in user_input):
        print("Invalid input! Please enter a string containing only '0's and '1's.")
        return
    
    if has_equal_ones_and_zeros(user_input):
        print("The string has an equal number of '1's and '0's.")
    else:
        print("The string does not have an equal number of '1's and '0's.")

if __name__ == "__main__":
    main()
