class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 完全数は数自身を除いた正の約数の和に等しい正の整数
        # 28 / 1 = 28
        # 28 / 2 = 14
        # 28 / 4 = 7
        # ....
        # と続いていく。
        # 加えて、これらの約数の和がnに等しいものを完全数をいう。

        # 普通にやるとメモリを使い果たしてしまう。
        # 約数を求める方法を考える必要がある。

        # 1は確定で、自身は含まないので、range(2, num)
        # 初期値はans = 1
        # filterはgenerator
        # if num % x == 0
        
        if num <= 1:
            return False
        ans=1
        print(num**0.5)
        print(num//2)

        for i in range(2,int(num*0.5)+1): 
            if num % i==0:
                print(ans, i,  num//i)
                ans += i + num//i # 外と外、うちとうちというふうに計算できるようになる
                # しかし、0.5かけただけでは、反対が存在するため、さらにその半分で良い
                # https://www.keisan-mondai.com/1889.htm#:~:text=1%E3%81%8B%E3%82%89100%E3%81%BE%E3%81%A7%E3%81%AE%E5%92%8C%E3%81%AF5050%E3%81%A7%E3%81%99%E3%80%82,-%E9%85%8D%E5%88%97%E9%96%A2%E6%95%B0%E3%82%92
                # ガウスの和と同じことをやってる
        
        return num == ans