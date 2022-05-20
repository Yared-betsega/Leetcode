# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        int_to_str = {
            0: '',
            1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred',
        1000: 'Thousand',
        1000000: 'Million',
        1000000000: 'Billion'
        }
        
        def createHundreds(s):
            s = str(s)
            if len(s) == 1:
                return int_to_str[int(s[0])]
            elif len(s) == 2:
                if int(s) not in int_to_str:
                    return int_to_str[int(s[0]+'0')] +" "+ int_to_str[int(s[1])]
                else: return int_to_str[int(s)]
            else:
                return int_to_str[int(s[0])] + ' Hundred ' + createHundreds(int(s[1:]))
        pref = 0
        num = str(num)
        temp = ''
        answer = ''
        for i in range(len(num)-1, -1, -1):
            temp += (num[i])
            if len(temp) == 3 or i == 0:
                x = createHundreds(int(temp[::-1])) 
                if x != "":
                    if pref == 1:
                        x += " "+ int_to_str[1000]+" "
                    elif pref == 2:
                        x += " "+ int_to_str[1000000]+" "
                    elif pref == 3:
                        x += " "+ int_to_str[1000000000]+" "
                answer = x + answer
                temp = ''
                pref += 1
                
        res = list(filter(lambda x: x != '', answer.split(' ')))
        return " ".join(res)
        
