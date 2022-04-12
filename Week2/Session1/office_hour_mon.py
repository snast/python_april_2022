students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan', 'grades': 100},
         {'first_name' : 'John', 'last_name' : 'Rosales','grades': 88},
         {'first_name' : 'Mark', 'last_name' : 'Guillen','grades': 96},
         {'first_name' : 'KB', 'last_name' : 'Tonel','grades': 45}
]

for student in students:
    print(student['first_name'])
    # student = students[0]
    # student['key'] = value
    # student is dictionary, so we can do whatever with student that a dict can

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
        #item['grades']

iterateDictionary2('grades', students)


# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function 
# prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# how do we print out all items in a list
# my_list = ['Michael', 'John', 'Mark', 'KB']
# for name in my_list:
#     print(name)
#     #something = my_list[0]
#     #something = my_list[1]
#     #something = my_list[len(my_list)-1]

# my_dict = {'first_name':  'Sal', 'last_name' : 'Nast'}
# print(my_dict['first_name'])