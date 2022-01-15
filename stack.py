class Stack:
    #ustaw "stack" na initialval
    def __init__(self, initialVal=[]):
        self.stack = initialVal

    #dodaj element do stacka appendem
    #zwroc go
    def push(self, element):
        self.stack.append(element)
        return self.stack

    #usun element na koncu stacka
    def pop(self):
        return self.stack.pop(-1)

    #zwroc kopie stacka
    def checkStack(self):
        print(self.stack)

    #zwroc wartosc na szczycie stacka
    def checkTop(self):
        print(self.stack[-1])