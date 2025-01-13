print("Name: Sufyan Ansari Roll: 5008")
class ThreeConsecutiveOnesMachine:
    def __init__(self):
        self.state = 'S0'  # Initial state
    def transition(self, input_char):
        if self.state == 'S0':
            if input_char == '1':
                self.state = 'S1'
            else:
                self.state = 'S0'
        elif self.state == 'S1':
            if input_char == '1':
                self.state = 'S2'
            else:
                self.state = 'S0'
        elif self.state == 'S2':
            if input_char == '1':
                self.state = 'S3'  # Accepting state
            else:
                self.state = 'S0'
    def is_accepted(self):
        return self.state == 'S3'

    def reset(self):
        self.state = 'S0'
def main():
    machine = ThreeConsecutiveOnesMachine()
    input_string = input("Enter a binary string (composed of 0s and 1s): ")

    for char in input_string:
        if char not in '01':
            print("Invalid input. Please enter a binary string.")
            return
        machine.transition(char)
    if machine.is_accepted():
        print("The input string is accepted (contains three consecutive '1's).")
    else:
        print("The input string is rejected (does not contain three consecutive '1's).")
if __name__ == "__main__":
    main()
