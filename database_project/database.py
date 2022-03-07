print("This is the blood_calculator module and python calls it {}".format(__name__))

import blood_calculator.py
import analysis 

HDL_value = 55
classification = blood_calculator.check_HDL()
print("55 is {}".format(classification))
