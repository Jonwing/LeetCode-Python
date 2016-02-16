Nim Game
====

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

---

### 想法 

##### 初始情况

n = 1, 2, 3时，无论如何都可以赢。 n = 4时，无论如何都赢不了。

推广到一般情况，有n个石头时，作为第一个拿石头的人A，策略无非是拿1颗、拿2颗、拿3颗。 则B面对的石头数将会是(n-1), (n-2), (n-3)。在B取完石头后，A将面临9种情况：

|第一次A拿| 第二次B拿|
|-----|-----|
|n-1 | n-2, n-3, n-4|
|n-2 | n-3, n-4, n-5|
|n-3 | n-4, n-5, n-6|

##### 如何保证赢？

选择一个数量的石头之后，确保无论下一轮B采取何种策略，都可以赢，也就是

> f(n-1) = f(n-2)&&f(n-3)&&f(n-4)

> f(n-2) = f(n-3)&&f(n-4)&&f(n-5)

> f(n-3) = f(n-4)&&f(n-5)&&f(n-6)

而这三种策略种，只要有一种策略可以保证赢就可以了。因此总的来说，就是

> f(n) = (f(n-2)&&f(n-3)&&f(n-4)) || (f(n-3)&&f(n-4)&&f(n-5)) || (f(n-4)&&f(n-5)&&f(n-6))

观察上式，f(n-4) = False 的时候， f(n)一定是 False，也就是肯定赢不了。
根据初始情况和上式，f(5), f(6), f(7) 也是True， f(8)是False。规律就是f(5), f(6), f(7), f(8)可以转化成f(1), f(2), f(3), f(4) , 也就是所有f(4n+1),f(4n+2), f(4n+3)都是True， 而f(4n)必然是False。因此只要n不能被4整除，就可以赢了。
