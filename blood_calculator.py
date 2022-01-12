def interface():
    print('Blood Teat Analysis')
    keep_running = True
    while keep_running: 
        print('Options: ')
        print('9-Quit')
        choice = input("Enter your choice: ")
        if choice == '9': 
            keep_running = False
    return 

def accept_input(test_name): 
    entry = input("Enter the test result here: ")
    return int(entry)


def check_HDL(HDL_value): 
    if HDL_value >= 60: 
        answer = 'Normal'
    elif HDL_value >= 40 && < 60: 
        answer = 'Borderline Low'
    else: 
        answer = 'Low'
    return answer

interface()

