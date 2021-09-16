# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# 1 <= num <= 3999

def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    roman_values = roman_map.keys()
    sol = ''
    for i, digit in enumerate(str(num)):
        digit = int(digit)
        powerten = len(str(num)) - i
        romans = [val for val in roman_values if len(str(val)) == powerten]

        if len(romans) == 1:
            oneten = romans[0]
        else:
            oneten, fiveten = [
                val for val in roman_values if len(str(val)) == powerten]

        if digit > 0 and digit < 4:
            sol += roman_map[oneten] * digit
        elif digit == 4:
            sol += roman_map[oneten] + roman_map[fiveten]
        elif digit > 4 and digit < 9:
            sol += roman_map[fiveten] + roman_map[oneten] * (digit - 5)
        elif digit == 9:
            sol += roman_map[oneten] + roman_map[oneten * 10]
    return sol


print(intToRoman(3999))
