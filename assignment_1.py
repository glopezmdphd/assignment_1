# Part 1
my_string = "buttermilk"
my_integer = 4
my_float = 3.14

# Part 2
int_1 = 2
int_2 = 4
temp_var = int_1 + int_2
# temp_var should be equal to 6
print("The value of int_1 + int_2 is:", temp_var)

# Part 3
float_1 = 3.14
float_2 = 2.718
temp_float_var = float_1 + float_2
# temp_float_var should be equal to the sum; 5.858
print("The value of float_1 + float_2 is:", temp_float_var)

# Part 4
string_1 = "I like to eat "
string_2 = "dark chocolate"
temp_string = string_1 + string_2
# temp_string should print out, I like to eat dark chocolate
print(temp_string)

# Part 5
sum_int_float = int_1 + float_1
# I expect the sum of an integer and a float to be, 5.14
print("The value of the third variable is:", sum_int_float)
# I expect the sum of an integer and a float to be a type float

# Part 6
#sum_int_and_string = int_1 + string_2
# I expect an error message to be displayed
#print(sum_int_and_string)
# The output was; TypeError: unsupported operand type(s) for +: 'int' and 'str'.
# The + operator is context-dependent in Python, and its behavior depends on the types of the operands.

print("my_string is type: ", type(my_string), "my_int is type ", type(my_integer), "my_float is type ", type(my_float))
int_as_string = "12"
print(type(int_as_string))
int_variable = int(int_as_string)
print(int_variable)
product = 5 * 7.654321
print(round(product, 3))
my_name = input("Enter your name:")
print(my_name)
favorite_number = input("Enter your favorite number:")
print(favorite_number)
# Favorite number is likely a string
print(type(favorite_number))
# In Python, the input() function always returns the entered value as a string, regardless of
# whether the user enters a number, text, or any other input.
number_1 = input("What is your first Integer number:")
number_2 = input("What is your second Integer number:")
sum_number_1_2 = number_1 + number_2
# the output should be a string. entering 11 and 22 will give output 1122
print(sum_number_1_2)
# sum_number_1_2 will be another string, concatenating the first input with the second input
correct_sum = int(number_1) + int(number_2)
print(correct_sum)
