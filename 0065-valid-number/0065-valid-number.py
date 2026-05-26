class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

            elif ch in ['+', '-']:
                # sign is valid only at start or after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # dot cannot appear after exponent or twice
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in ['e', 'E']:
                # exponent must appear once and after a digit
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                seen_digit = False   # need digits after exponent

            else:
                return False

        return seen_digit