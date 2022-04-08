# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()    # output: good morning (repeated on 2 lines)
# be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# students[0]['first_name'] # -> 'michael'
# # students[0] -> dictionary 
# # dictionary['key'] = 'value'

# sports_directory['soccer'][0] # 'Messi'

# Given an integer, n , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# Positive number

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

def weird_number(n):
    if n%2 == 1:
        print("Weird")
    else:
        if n >=2 and n<=5:
            print("Not weird")
        elif n >=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

weird_number(24)
