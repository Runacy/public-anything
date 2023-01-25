class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        val_l = [i for i in range(2, num) if num % i == 0]
        ans = 1 + sum(val_l)
        
        return num == ans