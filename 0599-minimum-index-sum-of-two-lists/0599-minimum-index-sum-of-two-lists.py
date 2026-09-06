class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        com_strs = []
        least_idx_sum = float('inf')

        # Step 1: Pre-process list1 into a lookup table
        for i, restaurant in enumerate(list1):
            hash_map[restaurant] = i

        # Step 2: Stream through list2 and evaluate matches
        for j, restaurant in enumerate(list2):
            if restaurant in hash_map:
                curr_sum = hash_map[restaurant] + j
                
                if curr_sum < least_idx_sum:
                    com_strs = [restaurant]
                    least_idx_sum = curr_sum
                elif curr_sum == least_idx_sum:
                    com_strs.append(restaurant)

        return com_strs