import requests

jn187 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jn187")
print(jn187.text)

yc508 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/yc508")
print(yc508.text)

id_donor = jn187['Donor']
donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(id_donor))
print(donor.text)

