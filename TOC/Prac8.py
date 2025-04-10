import re
print("Mohammad Husain 5042")
def is_valid_string(s):

    pattern = r'^(a+b+c+)$'

    match = re.match(pattern, s)
    if match:
    
        count_a = s.count('a')
        count_b = s.count('b')
        count_c = s.count('c')
      
        return count_a == count_b == count_c
    return False

test_string = input("Enter the string: ")


if is_valid_string(test_string):
    print(f"{test_string} is accepted.")
else:
    print(f"{test_string} is rejected.")
