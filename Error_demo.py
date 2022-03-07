def syntax_error():
    list = ""
    list.append("error")
    return list

    
def calcu_square_root(n):

    try:
        from my_calculator import sqrt
    except ModuleNotFoundError: 
            from math import sqrt
            print("my calculator module not available. Using default.")
    return sqrt(n)


def main():
    try:
        syntax_error()
    except AttributeError : 
        print("this list is a string")


if __name__ == "__main__":
    main()