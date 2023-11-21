'''
scope - LEGB
Local - defined within a function
Enclosing(nonlocal) -  in local scope of an enclosing function
Global - defined at begining of a module or with keyword global
Builtin - variables preassigned by python (like print(), input())
'''

# global variable
c = 1 # c is implicit global variable
def add():
#Unless defined locally, variable has global scope. Global variable can be read anywhere.
    print(c)
add()
def add():
     # increment c by 2
   # c = c + 2       #UnboundLocalError: local variable 'c' referenced before assignment
    print(c)        #
add()

# This is because we can only access the global variable but cannot modify it from inside the function.
# Local namespace supercedes global namespace!
#
# The solution for this is to use the global keyword.

def add():
    # use of global keyword
    global c        #refer to global c
    # increment c by 2
    c = c + 2
    print(c)

add()
print(c)
# Output: 3
def func1():
    g = 56

def func2():
    g = 34

g=100
print(g) #100
def func3():
    g = 23
    # use of nonlocal - refers to nearest scope (neither local, nor global)
    #nonlocal g #no binding for nonlocal 'g' found
    print(g) #23

    def func4():
        nonlocal g
        print(g)  #23

    func4()
func3()
print(g) #100

# def outer_function():
#     num = 20
#
#     def inner_function():
#         global num    #makes num accessible outside inner_function
#         #print (num) #NameError: name 'num' is not defined.
#         num = 25
#         print(num) #25
#     print("Before calling inner_function(): ", num) #20
#     inner_function() #25
#     print("After calling inner_function(): ", num) #20
#
#
# outer_function()
# print("Outside both function: ", num) #25. Because after declaring global this is the value assigned.

def outer_function():
   # global num
    num = 20

    def inner_function():
        nonlocal num    #points to num in outer_func
        print (num) #20
        num = 25
        print(num) #25
    print("Before calling inner_function(): ", num) #local scope of outer function = 20
    inner_function() #25
    print("After calling inner_function(): ", num) #local scope of outer function = 25


outer_function()
#print("Outside both function: ", num) #name 'num' is not defined.

a = 35
def outer():
    global a
    a = 25
    def inner1():
        def inner2():
            #nonlocal a  #no binding for nonlocal 'a' found because nonlocal = neither local nor global!
            a = 30

x = 'global x'

def test():
    x = 'local x'
    y = 'local y for test'
    print(x)

    def test2():
        print(x) #'local x'
        print(y) # 'local y for test'

    test2


test() #'local x'
print(x) #'global x'