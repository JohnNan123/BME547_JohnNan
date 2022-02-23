import requests

r = requests.get(
    "https://api.github.com/repos/octocat/hello-world/branches"
)


print(r)
print(type(r))
print("Status code = {}".format(r.status_code))
print("Text = {}".format(r.text))
answer = r.json()

if r.status_code != 200:
    print('there is a problem')
    print(r.text)
    exit()


for branch in answer: 
    print(branch['name'])