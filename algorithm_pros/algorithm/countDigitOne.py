"""
title：1~n整数中1出现的次数
writer：山客
date：2021.4.15
key：变量递推
example：
输入：n = 12
输出：5
tips：
① 简单做法（数组、转换类型判断）会超出内存限制
"""


class Solution:
    def countDigitOne(self, n: int) -> int:

        # 设数字 n 是个 x 位数，记 n 的第 i 位为 n[i]​
        # 则 n 可写为 n[0]~n[x - 1]​

        # digit - 个位、位因子
        # cur - 当前位，low - 低位，high - 高位
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0

        # 当高位和当前位都为0时，说明已经越过最高位了，因此跳出
        while high != 0 or cur != 0:
            if cur == 0:
                # 此cur位 1 出现的次数由high决定
                res += high * digit
            elif cur == 1:
                # 此cur位 1 出现的次数由high、low决定
                res += high * digit + low + 1
            else:
                # 此cur位 1 出现的次数由high位决定
                res += (high + 1) * digit
            # 将cur加入low，组成下轮low
            low += cur * digit
            # 下轮cur是本轮high的最低位
            cur = high % 10
            # 将本轮high最低位删除，得到下轮high
            high //= 10
            # 位因子每轮 * 10
            digit *= 10

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(12))
