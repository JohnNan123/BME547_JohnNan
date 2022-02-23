import requests

out_data = {
   "name": "Junyu Nan",
   "net_id": "jn187",
   "e-mail": "Junyu.nand@duke.edu"
}

r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)