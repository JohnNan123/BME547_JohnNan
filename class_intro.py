class Patient: 

    def __init__(self):
        self.name = name 
        self.id = id 
        self.age = age 
        self.tests = []

    def __repr__(self):
        return "Person: {}, {}".format(self.name, self.id)

    def output_person(self):
        outstring = "Name: {}\n".format(self.name)
        outstring += "Id: {}\n".format(self.id)
        outstring += "age: {}\n".format(self.age)
        outstring += "Test {}\n".format(self.tests)
        return outstring
        
def add_person(name, id, age):
    new_person = Patient(name, id, age)
    return new_person


def class_work():
    x = Patient()
    print(x.name)
    print(x.id)


if __name__ == "__main__":
    class_work()


