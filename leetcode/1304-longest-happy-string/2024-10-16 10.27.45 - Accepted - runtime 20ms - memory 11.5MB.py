class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        max_length = a + b + c  # Maximum possible length of the string
        lDString = []  # List to build the string

        # List of (count, character) tuples
        counts = [(a, 'a'), (b, 'b'), (c, 'c')]

        while sum(count for count, char in counts) > 0:
            # Sort the list by the count in descending order
            counts.sort(reverse=True, key=lambda x: x[0])

            # Find the last two characters in the current string
            last_two = ''.join(lDString[-2:])

            # Try to add the character with the highest count
            if counts[0][0] > 0 and last_two != counts[0][1] * 2:
                lDString.append(counts[0][1])
                counts[0] = (counts[0][0] - 1, counts[0][1])
            elif counts[1][0] > 0 and last_two != counts[1][1] * 2:
                lDString.append(counts[1][1])
                counts[1] = (counts[1][0] - 1, counts[1][1])
            elif counts[2][0] > 0 and last_two != counts[2][1] * 2:
                lDString.append(counts[2][1])
                counts[2] = (counts[2][0] - 1, counts[2][1])
            else:
                # If we cannot add any valid characters, break the loop
                break

        return ''.join(lDString)
