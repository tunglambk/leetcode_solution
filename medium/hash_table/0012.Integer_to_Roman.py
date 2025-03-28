class Solution:
    def intToRoman(self, num: int) -> str:
        
        int_roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: 'I',
        }
        
        roman_num = ''
        
        for digit in int_roman:
            roman_num += num//digit * int_roman[digit]
            num %= digit
        return roman_num
