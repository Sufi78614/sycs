print("Mohammad Husain 5042")
def turing_string(s):
    state = 0  
    count_a = count_b = count_c = 0  
    
    for char in s:
        if state == 0:
            if char == 'a':
                state = 1
                count_a += 1
            else:
                return False  
        
        elif state == 1:
            if char == 'a':
                count_a += 1
            elif char == 'b':
                state = 2
                count_b += 1
            else:
                return False  
        
        elif state == 2:
            if char == 'b':
                count_b += 1
            elif char == 'c':
                state = 3
                count_c += 1
            else:
                return False  
        
        elif state == 3:
            if char == 'c':
                count_c += 1
            else:
                return False  

    if count_a == count_b == count_c and state == 3:
        return True
    else:
        return False

# Input and checking
test_string = input("Enter the string: ")

if turing_string(test_string):
    print(f"{test_string} is accepted.")
else:
    print(f"{test_string} is rejected.")
