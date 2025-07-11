class Solution(object):
    def romanToInt(self, s):
        answer = list(s)
        print(answer, "Answer")

        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0

        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        total += values[s[-1]]

        return total


def main():
    s = Solution()
    return s.romanToInt('IV')

print(main())
