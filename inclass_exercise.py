from urllib import request


import requests

input_message = {
    'user': 'Junyu Nan',
    'message': 'you are handsome'
}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = input_message)
print(r.text)

g = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Mario_Chem")
print(g.text)s