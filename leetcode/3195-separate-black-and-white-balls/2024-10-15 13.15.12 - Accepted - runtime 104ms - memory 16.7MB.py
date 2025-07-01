class Solution(object):
    def minimumSteps(self, s):
        swaps = 0
        num_zeros = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                swaps += num_zeros
            else:
                num_zeros += 1
        return swaps
    