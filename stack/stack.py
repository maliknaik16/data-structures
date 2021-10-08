
class Stack:

    def __init__(self):
        """
        Initialize the stack class.
        """

        self.stack = []


    def push(self, element):
        """
        Pushes the element to the top of the stack.

        Parameters:
        ------------

        element :
            Element of any type to be pushed to the top of the stack.
        """

        self.stack.append(element)

    def peek(self):
        """
        Returns the to element from the stack.
        """

        return self.stack[-1]

    def pop(self):
        """
        Pops and returns the top element of the stack.
        """

        top = self.stack[-1]

        self.stack.pop()

        return top

    def empty(self):
        """
        Returns whether the stack is empty or not.
        """

        return (len(self.stack) == 0)


    def show(self):
        """
        Prints the stack.
        """

        if stack.empty():

            print('\tStack is empty.')

        else:

            i = len(self.stack) - 1

            while i > -1:

                print('\t|', self.stack[i], '|')

                i -= 1

stack = Stack()

stack.push(3)
stack.push(5)
stack.push(8)

print('After push: ')
stack.show()

stack.pop()
stack.pop()
stack.pop()

print('After 3 pops: ')
stack.show()

print('After and 2 pushes: ')
stack.push(1)
stack.push(3)

stack.show()

print('Peek:', stack.peek())

# Outputs:
#
# After push:
#     | 8 |
#     | 5 |
#     | 3 |
# After 3 pops:
#     Stack is empty.
# After and 2 pushes:
#     | 3 |
#     | 1 |
# Peek: 3
