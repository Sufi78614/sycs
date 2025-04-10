print("Mohammad Husain 5042")
class FSM:
    def __init__(self):
        self.state = 'S0'  # Start in the initial state

    def transition(self, input_char):
        if self.state == 'S0':
            if input_char == '1':
                self.state = 'S1'
        
        elif self.state == 'S1':
            if input_char == '0':
                self.state = 'S2'
            # Remain in S1 if another '1' comes
        
        elif self.state == 'S2':
            if input_char == '1':
                self.state = 'S3'  # Reached "101"
            elif input_char == '0':
                self.state = 'S0'  # Reset since "101" is broken
        
        elif self.state == 'S3':  
            # Once "101" is matched, it should stay accepted
            self.state = 'S3'  

    def accepts(self, input_string):
        self.state = 'S0'  # Reset state before processing new input
        for char in input_string:
            self.transition(char)
        return self.state == 'S3'  # Accept if we end in state S3

# Example usage
fsm = FSM()
test_strings = ["1101", "101", "1001", "111", "0101", "1010"]

for s in test_strings:
    result = fsm.accepts(s)
    print(f"The string '{s}' is {'accepted' if result else 'not accepted'} by the FSM.")
