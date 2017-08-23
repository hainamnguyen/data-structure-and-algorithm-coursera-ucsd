# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    #text = input()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append([i, next])

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                print(i+1)
                break
            else:
                t = opening_brackets_stack.pop()[1] + next
                if t != '()' and t != '[]' and t != '{}':
                    print(i+1)
                    break
        if i == len(text)-1:
            if len(opening_brackets_stack) == 0:
                print('Success')
            else:
                print(opening_brackets_stack[0][0] + 1)
    # Printing answer, write your code here
