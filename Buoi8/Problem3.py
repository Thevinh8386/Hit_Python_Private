class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.stack) == self.capacity:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack rỗng, không thể xóa phần tử.")
            return None
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            print("Stack rỗng, không có phần tử trên cùng.")
            return None
        else:
            return self.stack[-1]


stack1 = MyStack(5)
stack1.push(1)
stack1.push(2)

print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())
print(stack1.pop())
