# my_dict = {
#     'name': 'Sal',
#     'age': 29,
#     'stack': 'Python'
# }

# # Sal is 29 years old and is taking Python
# #f-strings
# name = my_dict['name']
# age = my_dict['age']
# stack = my_dict['stack']
# my_string = f'{my_dict["name"]} is {my_dict["age"]} years old and is taking {my_dict["stack"]}'

# print(my_string)

# print(my_dict.keys())
# print(my_dict.values())
# for key in my_dict.keys():
#     print(key)

# num = 5
# num2 = 10
# while num <=10:
#     num += 1 # num = num +1
#     print(num)

# What is a function in coding?
# def sal_function():
#     # print("We are executing sal_function")
#     #set of instructions
#     pass

# sal_function()

# def add(a, b):
#     output = a+b
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(output)
#     return output

# sum = add(4321, 1234)
# print(sum)
# This function adds up to 3 numbers together
def add(a=1,b=1, c=0):
    return a+b
# print(add())
# print(add(3))
# print(add(3,4))
# print(add(b=4, a=10))
# print(add(4,10))
# print(add(4,10,100))
sals_variable = add()

print(sals_variable)
