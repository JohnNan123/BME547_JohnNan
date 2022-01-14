def interface():
    print('Blood Teat Analysis')
    keep_running = True
    while keep_running: 
        print('Options: ')
        print('''1-HDL_driver \n9-Quit''')
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





interface()

