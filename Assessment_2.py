# Addition Function
def add_numbers(first_number, second_number):
    return first_number + second_number


# Subtraction Function
def subtract_numbers(first_number, second_number):
    return first_number - second_number

#hello world example
# Multiplication Function
def multiply_numbers(first_number, second_number):
    return first_number * second_number


# Division Function
def divide_numbers(first_number, second_number):
    return first_number / second_number


# Function Calls
addition_result = add_numbers(10, 5)
subtraction_result = subtract_numbers(10, 5)
multiplication_result = multiply_numbers(10, 5)
division_result = divide_numbers(10, 5)


# Display Results
print("Addition :", addition_result)
print("Subtraction :", subtraction_result)
print("Multiplication :", multiplication_result)
print("Division :", division_result)


# Circle Area Function
def calculate_circle_area(radius):
    pi_value = 3.14
    return (pi_value * radius) ** 2


# Circle Circumference Function
def calculate_circumference(radius):
    pi_value = 3.14
    return 2 * pi_value * radius


# Function Calls
circle_area_result = calculate_circle_area(20)
circle_circumference_result = calculate_circumference(20)


# Display Results
print("Circle Area :", circle_area_result)
print("Circumference :", circle_circumference_result)

# Rectangle Area Function
def calculate_rectangle_area(length, breadth):
    return length * breadth


# Rectangle Perimeter Function
def calculate_rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# Function Calls
rectangle_area_result = calculate_rectangle_area(10, 5)
rectangle_perimeter_result = calculate_rectangle_perimeter(10, 5)


# Display Results
print("Rectangle Area :", rectangle_area_result)
print("Rectangle Perimeter :", rectangle_perimeter_result)

# Simple Interest Function

def calculate_simple_interest(principal_amount, interest_rate, time_period):
    simple_interest = (principal_amount * interest_rate * time_period) / 100

    return simple_interest


interest_result = calculate_simple_interest(100, 2, 2)

print("Simple Interest is", interest_result)