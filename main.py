# Calculator
from pyscript import display, document


def find_sum(e): # it finds the sum when adding the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def find_difference(e): # it finds the differece when subtracting the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def find_product(e): # it finds the product when multiplying the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def find_quotient(e): # it finds the quotient when dividing the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number / second_number

    display(f'The quotent of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def find_power(e): # it finds the power when the first number is raised by the second number
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number ** second_number

    display(f'The power of {first_number} raised to {second_number} is {sum}', target='result') # displays the answer

def find_floor_quotient(e): # it finds the rounded down quotient when dividing the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number // second_number

    display(f'The rounded down quotient of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def find_remainder(e): # it finds the remainder when dividing the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number % second_number

    display(f'The remainder of {first_number} and {second_number} is {sum}', target='result') # displays the answer

def clear_result(e): # clears the result but keeps the numbers
    document.getElementById('result').innerHTML = " " # clears the previous answer

    display(f'', target='result') # displays the answer