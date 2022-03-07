from inspect import classify_class_attrs
from multiprocessing.connection import answer_challenge

from inspect import classify_class_attrs
from multiprocessing.connection import answer_challenge


def interface():
    print('Blood Teat Analysis')
    keep_running = True
    while keep_running: 
        print('Options: ')
        print('1-HDL \n2-LDL \n3-Cholesterol \n9-Quit')
        choice = input("Enter your choice: ")
        if choice == '9': 
            keep_running = False
        elif choice == '1': 
            HDL_driver()
        elif choice == '2': 
            LDL_driver()
        elif choice == '3': 
            Cholesterol_driver()
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

def check_Cholesterol(Cholesterol_value): 
    if Cholesterol_value < 200:
        answer = 'Normal'
    elif Cholesterol_value >= 200 and Cholesterol_value <= 239: 
        answer = 'Borderline High'
    else: 
        answer = 'High'
    return answer

def Cholesterol_driver(): 
    Cholesterol_value = accept_input("Cholesterol")
    classification = check_Cholesterol(Cholesterol_value)
    print_result("Cholesterol", Cholesterol_value, classification)
    
interface()

if __name__ == "__main__":
    interface()

