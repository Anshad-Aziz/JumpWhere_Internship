
2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 
class ParenthesisValidator:
    def _init_(self, string):
        self.string = string
        self.stack = []
    def is_valid(self):
        for char in self.string:
            if char in ["(", "{", "["]:
                self.stack.append(char)
            elif char in [")", "}", "]"]:
                if len(self.stack) == 0 or self.stack.pop() != char:
                    return False

        return len(self.stack) == 0
parenthesis_validator = ParenthesisValidator("()")
print(parenthesis_validator.is_valid()) 
parenthesis_validator = ParenthesisValidator("({[]})")
print(parenthesis_validator.is_valid())  
parenthesis_validator = ParenthesisValidator("[)")
print(parenthesis_validator.is_valid())
