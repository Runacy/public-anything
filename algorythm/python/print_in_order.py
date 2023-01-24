from threading import Lock

# 問題
# https://leetcode.com/problems/print-in-order/

class Foo:
  def __init__(self):
    # 2つロックをかける
    print(1)
    self.locks = (Lock(), Lock())
    # ロックを取得する
    # 順番にロックを解除していく
    print(2)
    self.locks[0].acquire()
    print(3)
    self.locks[1].acquire()
    print(4)
    pass


  def first(self, printFirst: 'Callable[[], None]') -> None:
    print(5)
    # printFirst() outputs "first". Do not change or remove this line.
    printFirst()
    print(6)
    self.locks[0].release()
    # releaseしたら、次withで指定してるところがロックを取得できる。
    print(7)
      



  def second(self, printSecond: 'Callable[[], None]') -> None:
    # printSecond() outputs "second". Do not change or remove this line.
    print(8)
    with self.locks[0]:
      print(8)
      printSecond()
      print(9)
      self.locks[1].release()
      print(10)

      
      


  def third(self, printThird: 'Callable[[], None]') -> None:
    print(11)
    # printThird() outputs "third". Do not change or remove this line.
    with self.locks[1]:
      print(12)
      printThird()
      print(13)
