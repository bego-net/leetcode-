class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a, b, start):
            while start < n:
                c = a + b
                s = str(c)

                if not num.startswith(s, start):
                    return False

                start += len(s)
                a, b = b, c

            return True

        for i in range(1, n):
            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]

                # leading zero check
                if len(first) > 1 and first[0] == '0':
                    break

                if len(second) > 1 and second[0] == '0':
                    continue

                if valid(int(first), int(second), j):
                    return True

        return False