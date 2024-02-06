class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
# s =Stack()
# print(s.items)
# print(s.is_empty())
# print(s.push('Pyae'))
# print(s.items)
# # print(s.pop())
# # print(s.items)
# print(s.peek())
# print(s.items)
# print(s.size())

