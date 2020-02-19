'''
# integer to roman
class Roman():
    def __init__(self,number):
        self.number = number
    
    def convertToroman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  self.number > 0:
            for _ in range(self.number // val[i]):
                roman_num += syb[i]
                self.number -= val[i]
            i += 1
        return roman_num

rom = Roman(100)
print(rom.convertToroman())
'''

# 