# print('Hello Damilare')
# print(30 +30)
# print('''
      
#             fsdkfnsfsdklfnsdksdf
#             kdfdfmkdsfsdlfkdkdf
#             dmfnklsdfnldfnsdkdkm
#             ,d,fmsfdfmlsd;fm;ldf
      
# ''')

# Python variables
# container = 20
# print(container)
name = 'Babatunde'
age = 20
# print('Hello '+name)
# print('Hello',name)
# print('56'+ '67')

# print('My name is',name,'I am',age)
# print('my name is '+name+' I am '+ str(age))

NoOfStudent = '' #Pascal casing
myFirstName = '' #camel casing
no_of_student = '' #snake casing 

# multiple variable declaration

# x, y, z = 10, 23, 45

# multiple value, single variable declaration
x = 10, 23, 45

firstName, lastName = 'Damilare', 'Arise'
# print(firstName)

# Single value but multiple variable

# x = y = z = 20
# print(z)

# types of variables 
# 1. global variable
# 2. local variable

x = 5 # global variable

def add():
    global y
    y = 30 #local variable
    print(x + y)

# add()


def sub():
    print(x - y)

# sub()
    
# username = input('Username: ')
# first_value = input('First value: ')
# second_value = input('Second value: ')
# answer = int(first_value) + int(second_value)

# print(f'Hello {username}, if your inputted values are added together your answer is {answer}')


# PYTHON DATATYPES
'''
1. Text type: str(), e.g 'Damilare', 'True', '45'
2. Number type:
    i. Integers; int() e.g 4, 45, 678
    ii. Float; float() e.g 4.5, 6.006
    iii. Complex; complex() e.g 1 + 3j

3. Boolean: bool() e.g True, False
4. sequence type: 
    i. list; list() e.g ['Rice', 'Beans', 'Yam', 5000]
    ii. Tuple; tuple() e.g ('Rice', 'Beans', 'Yam', 5000)
    iii. range; range() e.g range(20), range(1, 21), range(1, 20, 2)

5. set types: set() e.g {'Boluwatife', 'Azeez', 'Babatunde', 'Temitayo'}
6. mapping type: 
    dictionary: dict(key = value) e.g {'name':'Ade', 'age':20, 'course':'datascience'}

'''    
# val = tuple(range(1, 21, 2))
val = {'Boluwatife', 'Azeez', 'Babatunde', 'Temitayo'}
val2 = {5, 6, 4, 2, 1, 7, 9, 8, 3}
# print(val2)
# print(type(val))

# val3 = ['Rice', 'Beans', 'Yam', 5000]
# username = 'Damilare' # ['D', 'a', 'm', ... ]
# print(val3)
# val3[2] = 'Potato'
# print(val3)
# print(val3[1][0])
# print(username[3])


details = {'name':'Ade', 'age':20, 'course':'datascience'}
# print(type(details))
