# Accessing a Global Variable from a Function
x = 7

def access_global():
    print('x printed from access_global:', x)

access_global()

def try_to_modify_global():
    x = 3.5
    print('x printed from try_to_modify_global:', x)

try_to_modify_global()

print(x)

def modify_global():
    global x;
    x = 'hello'
    print('x printed from modify_global:', x)

modify_global()

print(x)

# Shadowing Functions
sum = 10 + 5
print(sum)

print(sum([10, 5])) #will give error because we have overridden python sum method

type(sum) #builtin_function_or_method
