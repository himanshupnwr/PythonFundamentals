# 5.11 Simulating Stacks with Lists
stack = []

stack.append('red')

print(stack)

stack.append('green')

print(stack)

stack.pop()

print(stack)

stack.pop()

print(stack)

stack.pop()

#['red']
#['red', 'green']
#['red']
#[]
#IndexError: pop from empty list
