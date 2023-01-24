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
        res = 1
        tmp = []
        def f(res, x):
            res += x
            tmp.append(res)
            return res
        [f(res, x) for x in range(2, num//2 + 1) if num % x == 0]
        print(tmp)


# これはx
# 10000000くらいなら回せるけどなあ


if __name__ == "__main__":
    s = Solution()
    print(s.checkPerfectNumber(28))