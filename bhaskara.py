import math
import csv

def main():
    print_elements('header')
    a = float(input('Type the A value: '))
    b = float(input('Type the B value: '))
    c = float(input('Type the C value: '))  

    delta = get_delta(a, b, c)
    x1 = get_first_x(a, b, delta)
    x2 = get_second_x(a, b, delta)

    print(f'\nIn the {a}x² + ({b}x) + ({c}) equation, the result of Bhaskara formula is: ') 
    print(f'x1 = {x1:.02f} and x2 = {x2:.02f}') 

    print_elements('footer')

def get_delta(a, b, c):
    delta = (b**2) - 4 * (a * c)
    return delta

def get_first_x(a, b, delta):
    x = 0
    if delta > 0:
        x = ((-1 * b) + (math.sqrt(delta)))/2 * a
    elif delta == 0:
         x = (-1 * b)/2 * a
    elif delta < 0:
        print('Delta under zero')
    return x
    
def get_second_x(a, b, delta):
    x = 0
    if delta > 0:
        x = ((-1 * b) - (math.sqrt(delta)))/2 * a
    elif delta == 0:
        x = (-1 * b)/2 * a
    elif delta < 0:
        print('Delta under zero')
    return x

def write_csv(a, b, c, delta, x1, x2):
    pass

def read_csv():
    pass


def print_elements(option): 
    break_line = "\n***********************************************\n"
    header       = "*   Welcome to the Bhaskara Program!     *"
    footer       = "* Thanks for using the Bhaskara Program! *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")


if __name__ == "__main__":
    main()