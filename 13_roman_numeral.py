class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        print(romanMap)

        value = 0

        for index, char in enumerate(s):
            romanValue = romanMap[char]
            if (index != (len(s) - 1) and romanValue < romanMap[s[index + 1]]):
                value -= romanValue
            else:
                value += romanMap[char]

        return value
