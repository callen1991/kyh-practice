from calc import add, subtract, multiply, divide, result



def run():


    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 multiply numbers")
    print("4 divide numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))


    if answer == "1":
        result = add(a, b)
    if answer == "2":
        result = subtract(a, b)
    if answer == "3":
        result = multiply(a, b)
    if answer == "4":
        result = divide(a, b)

    print(f"Result = {result}")
if __name__ == '__main__':
    run()
