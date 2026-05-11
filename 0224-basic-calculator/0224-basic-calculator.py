class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for char in s:

            if char.isdigit():
                number = number * 10 + int(char)

            elif char == '+':
                result += sign * number
                number = 0
                sign = 1

            elif char == '-':
                result += sign * number
                number = 0
                sign = -1

            elif char == '(':
                # Save current state
                stack.append(result)
                stack.append(sign)

                # Reset for new expression
                result = 0
                sign = 1

            elif char == ')':
                result += sign * number
                number = 0

                # First pop sign
                result *= stack.pop()

                # Then previous result
                result += stack.pop()

        return result + sign * number