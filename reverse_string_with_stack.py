from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        return self.container.append(value)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return self.container == 0

    def size(self):
        return len(self.container)


def reverse_string(input_string):
    input_string = input_string.strip()
    stack = Stack()
    for i in input_string:
        stack.push(i)
    reversed_string = ""
    while stack.size() != 0:
        reversed_string += stack.pop()
    a = reversed_string.split(" ")
    return "".join(a)


if __name__ == "__main__":
    print(reverse_string("I love Nepal"))
