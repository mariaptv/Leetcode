class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack is None:
            self.stack.append(x)
            return

        self.stack.append(0)
        before = self.stack[0]
        self.stack[0] = x

        for i in range(1, len(self.stack)):
             actual = self.stack[i]
             self.stack[i]=before
             before = actual


    def pop(self):
        """
        :rtype: int
        """
        if self.stack is None:
            return None
        new = []
        result = self.stack[0]
        for i in range(1, len(self.stack)):
            print(self.stack[i])
            new.append(self.stack[i])

        self.stack = new
        return result



    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(3)
print(obj.stack)
obj.pop()
obj.pop()
print(obj.stack)