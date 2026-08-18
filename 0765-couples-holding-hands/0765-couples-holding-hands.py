# Python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        n = len(row)
        position = [0] * n

        # Map each person to their seat index
        for i in range(n):
            position[row[i]] = i

        # Process pairs of seats
        for i in range(0, n, 2):
            first = row[i]
            second = row[i + 1]
            expected_second = first ^ 1  # Partner of first person

            if second != expected_second:
                swaps += 1
                partner_index = position[expected_second]

                # Swap second person with the correct partner
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]

                # Update position map after swap
                position[second] = partner_index
                position[expected_second] = i + 1

        return swaps