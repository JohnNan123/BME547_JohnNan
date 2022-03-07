def get_input():
    point1 = input("enter point as formate x1,y1. \n")
    point2 = input("enter point as formate x2,y2. \n") 
    input_x = input("enter your input x \n") 
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    tuble_point1 = (x1, y1)
    tuble_point2 = (x2, y2)
    input_x = float(input_x)
    return tuble_point1, tuble_point2, input_x

def linear_function(point1, point2, input_x):
    y = (input_x - point2[0])/ (point1[0] - point2[0]) * (point1[1] - point2[1]) + point2[1]
    return y

    tuble_point1, tuble_point2, input_x = get_input()
    y = linear_function(tuble_point1, tuble_point2, get_input)
    print(y)
    
if __name__ == "__main__":
    point1, point2, input_x = get_input()
    y = linear_function(point1, point2, input_x)
    print("your y is ", y)