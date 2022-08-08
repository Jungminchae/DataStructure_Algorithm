class Solution:
    def intToRoman(self, num: int) -> str:
        def transfer(v, level_1, level_2, roman_1, roman_2, roman_3, roman_4):
            ret =""
            if int(v) < level_1:
                for _ in range(int(v[0])):
                    ret = roman_1 + ret
            elif int(v) == level_1:
                ret = roman_2 + ret
            elif int(v) < level_2:
                loop = int(v[0]) % 5
                for _ in range(loop):
                    ret = roman_1 + ret
                ret = roman_3 + ret
            elif int(v) == level_2:
                ret = roman_4
            return ret
        
        str_num = str(num)
        str_num = list(map(lambda x: x, str_num))
        nums = []
        for i, s in enumerate(str_num[::-1]):
            for _ in range(i):
                s += "0"
            nums.insert(0, s)
        result = ""
        while nums:
            value = nums.pop()
        
            # 4 case
            if len(value) ==1:
                ret = transfer(value, 4, 9, "I", "IV", "V", "IX")
            elif len(value) ==2:
                ret = transfer(value, 40, 90,"X", "XL", "L", "XC")
            elif len(value) ==3:
                ret = transfer(value, 400, 900,"C", "CD", "D", "CM")
            else:
                ret = ""
                for _ in range(int(value[0])):
                    ret = "M" + ret
            result = ret + result
        return result