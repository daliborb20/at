import copy
def eggs(cheese):
    cheese.append("hello")


spam = [1,2,3]

eggs(spam)

print(spam)

novVarijabla = copy.deepcopy(spam)#dodeljuje kopiju bez referenciranja sa starom
