"""
title: 平均等待时间
writer: m14
date: 2024.4.10
key：
example:
输入：customers = [[5,2],[5,4],[10,3],[20,1]]
输出：3.25000
解释：
1) 第一位顾客在时刻 5 到达，厨师拿到他的订单并在时刻 5 立马开始做菜，并在时刻 7 完成，第一位顾客等待时间为 7 - 5 = 2 。
2) 第二位顾客在时刻 5 到达，厨师在时刻 7 开始为他做菜，并在时刻 11 完成，第二位顾客等待时间为 11 - 5 = 6 。
3) 第三位顾客在时刻 10 到达，厨师在时刻 11 开始为他做菜，并在时刻 14 完成，第三位顾客等待时间为 14 - 10 = 4 。
4) 第四位顾客在时刻 20 到达，厨师拿到他的订单并在时刻 20 立马开始做菜，并在时刻 21 完成，第四位顾客等待时间为 21 - 20 = 1 。
平均等待时间为 (2 + 6 + 4 + 1) / 4 = 3.25 。
thinking：
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = customers[0][0]
        times = []

        for customer in customers:
            curr = max(customer[0], curr)
            
            time = customer[1] + curr - customer[0]
            times.append(time)
            curr += customer[1]

        return sum(times) / len(times)
