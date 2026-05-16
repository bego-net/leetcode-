class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()

                # truncate toward zero
                stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack[-1]