from inspect import classify_class_attrs
from re import L


def interface():
    print('Blood Teat Analysis')
    keep_running = True
    while keep_running: 
        print('Options: ')
        print('1-HDL \n2-LDL \n9-Quit')
        choice = input("Enter your choice: ")
        if choice == '9': 
            keep_running = False
        elif choice == '1': 
            HDL_driver()
        elif choice == '2': 
            LDL_driver()
    return 

def accept_input(test_name): 
    entry = input("Enter the {} test result here: ".format(test_name))
    return int(entry)

def print_result(test_name, test_vaule, test_class): 
    out_string = "The test value of {} for {} is {}.".format(test_vaule, test_name, test_class)
    print(out_string)


def check_HDL(HDL_value): 
    if HDL_value >= 60: 
        answer = 'Normal'
    elif HDL_value >= 40 and HDL_value < 60: 
        answer = 'Borderline Low'
    else: 
        answer = 'Low'
    return answer

def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)

def check_LDL(LDL_value): 
    if LDL_value < 130: 
        answer = 'Normal'
    elif LDL_value < 159 and LDL_value >= 130: 
        answer = 'Broadline High'
    elif LDL_value < 189 and LDL_value >= 160: 
        answer = 'High'
    else: 
        answer = 'Very High'
    return answer

def LDL_driver(): 
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)


interface()

