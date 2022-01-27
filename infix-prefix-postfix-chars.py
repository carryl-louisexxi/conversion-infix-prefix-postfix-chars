from abc import ABC, abstractmethod
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators = ['+', '-', '*', '/', '^']


class Expression:
    def isOpeningParenthesis(self, top):
        return True if top == '(' else False

    def isClosingParenthesis(self, top):
        return True if top == ')' else False

    def reverse(self, string):
        reversed = ""
        for st in string:
            if self.isOpeningParenthesis(st):
                st = ')'
            elif self.isClosingParenthesis(st):
                st = '('
            reversed = st + reversed
        return reversed


class Infix(Expression):
    def __init__(self):
        self.string = ""
        self.result = ""
        self.stack = []
        self.isPostfix = False

    def set(self, string):
        self.string = string

    def isHigherPrecedence(self, top, x):
        if self.isOpeningParenthesis(top):
            return False
        if self.isPostfix:
            if precedence[top] == precedence[x]:
                return True
        if precedence[top] > precedence[x]:
            return True
        return False

    def convert(self):
        for x in self.string:
            if x.isalpha():
                self.result += x

            elif x in operators:
                while self.stack and self.isHigherPrecedence(self.stack[-1], x):
                    self.result += self.stack[-1]
                    self.stack.pop()
                self.stack.append(x)

            elif self.isOpeningParenthesis(x):
                self.stack.append(x)

            elif self.isClosingParenthesis(x):
                while self.stack and not self.isOpeningParenthesis(self.stack[-1]):
                    self.result += self.stack[-1]
                    self.stack.pop()
                self.stack.pop()

        while self.stack:
            self.result += self.stack[-1]
            self.stack.pop()

        try:
            return self.result
        except:
            return 'Invalid String'

    def toPrefix(self):
        self.isPostfix = False
        self.string = self.reverse(self.string)
        return self.reverse(self.convert())

    def toPostfix(self):
        self.isPostfix = True
        return self.convert()

    def execute(self):
        print("Convert to? \n1. Prefix \n2. Postfix")
        try:
            choice = int(input('Choice: '))
        except:
            print('Value Error!')
        else:
            if choice == 1:
                return self.toPrefix()
            elif choice == 2:
                return self.toPostfix()
            else:
                return "Choice Out of Range"


class Prefix(Expression):
    def __init__(self):
        self.string = ""
        self.result = ""
        self.stack = []
        self.isPostFix = False

    def set(self, string):
        self.string = string

    def convert(self):
        for x in self.string:
            if x.isalpha():
                self.stack.append(x)
            elif x in operators:
                try:
                    op1 = self.stack[-1]
                    self.stack.pop()
                    op2 = self.stack[-1]
                    self.stack.pop()
                    if self.isPostFix:
                        exp = op1 + op2 + x
                    else:
                        exp = '(' + op1 + x + op2 + ')'
                    self.stack.append(exp)
                except:
                    return 'Invalid String'

        try:
            return self.stack[-1]
        except:
            return 'Invalid String'

    def toInfix(self):
        self.isPostFix = False
        self.string = self.reverse(self.string)
        return self.convert()

    def toPostfix(self):
        self.isPostFix = True
        self.string = self.reverse(self.string)
        return self.convert()

    def execute(self):
        print("Convert to? \n1. Infix \n2. Postfix")
        try:
            choice = int(input('Choice: '))
        except:
            print('Value Error!')
        else:
            if choice == 1:
                return self.toInfix()
            elif choice == 2:
                return self.toPostfix()
            else:
                return "Choice Out of Range"


class Postfix(Expression):
    def __init__(self):
        self.string = ""
        self.result = ""
        self.stack = []
        self.isInfix = False

    def set(self, string):
        self.string = string

    def convert(self):
        for x in self.string:
            if x.isalpha():
                self.stack.append(x)
            elif x in operators:
                try:
                    op1 = self.stack[-1]
                    self.stack.pop()
                    op2 = self.stack[-1]
                    self.stack.pop()
                    if self.isInfix:
                        exp = '(' + op2 + x + op1 + ')'
                    else:
                        exp = x + op2 + op1
                    self.stack.append(exp)
                except:
                    return 'Invalid String'

        try:
            return self.stack[-1]
        except:
            return 'Invalid String'

    def toInfix(self):
        self.isInfix = True
        return self.convert()

    def toPrefix(self):
        self.isInfix = False
        return self.convert()

    def execute(self):
        print("Convert to? \n1. Infix \n2. Prefix")
        try:
            choice = int(input('Choice: '))
        except:
            print('Value Error!')
        else:
            if choice == 1:
                return self.toInfix()
            elif choice == 2:
                return self.toPrefix()
            else:
                return "Choice Out of Range"


class Application:
    def main(self):
        while True:
            print("\n1. Convert String \n2. Quit")

            try:
                choice = int(input('Select: '))
            except:
                print('Value Error')
            else:
                if choice == 2:
                    return -1
                elif choice < 1 or choice > 2:
                    print('Index Out of Range')
                else:
                    string = input('Enter String: ')
                    self.evaluate(string)

    def evaluate(self, string):
        string = string.strip()
        contains_digit = any(map(str.isdigit, string))
        if not contains_digit:
            if (string[0].isalpha() or string[0] == '(') and (string[-1].isalpha() or string[-1] == ')'):
                infix = Infix()
                infix.set(string)
                print(infix.execute())
            elif string[0] in operators and string[-1].isalpha():
                prefix = Prefix()
                prefix.set(string)
                print(prefix.execute())
            elif string[0].isalpha() and string[-1] in operators:
                postfix = Postfix()
                postfix.set(string)
                print(postfix.execute())
            else:
                print('Invalid String')
        else:
            print('Invalid String')


app = Application()
app.main()
