class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 完全数は数自身を除いた正の約数の和に等しい正の整数
        # 28 / 1 = 28
        # 28 / 2 = 14
        # 28 / 4 = 7
        # ....
        # と続いていく。
        
        if num <= 1:
            return False
        ans=1

        for i in range(2,int(num**0.5)+1): 
            if num % i==0:
                ans += i + num//i 
        
        return num == ans