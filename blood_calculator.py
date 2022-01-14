from inspect import classify_class_attrs
from multiprocessing.connection import answer_challenge


def interface():
    print('Blood Teat Analysis')
    keep_running = True
    while keep_running: 
        print('Options: ')
        print('9-Quit')
        choice = input("Enter your choice: ")
        if choice == '9': 
            keep_running = False
        elif choice == '1': 
            HDL_driver()
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

def check_Cholesterol(Cholesterol_value): 
    if Cholesterol_value < 200:
        answer = 'Normal'
    elif Cholesterol_value >= 200 and Cholesterol_value <= 239: 
        answer = 'Borderline High'
    else: 
        answer = 'High'

def Cholesterol_driver(): 
    Cholesterol_value = accept_input("Cholesterol")
    classification = check_Cholesterol(Cholesterol_value)
    print_result("Cholesterol", Cholesterol_value, classification)


