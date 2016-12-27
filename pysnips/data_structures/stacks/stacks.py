from data_structures.stacks import Stack

stack = Stack(5)
stack.push("Python")
stack.push(1)
stack.push(dict(brian="Brian", lusina="Lusina", ombito="Ombito"))
stack.push((1, 5))
stack.push(range(5))

stack.display()

print(stack.filter_stack())
