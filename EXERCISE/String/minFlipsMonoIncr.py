"""
title：翻转字符
writer：山客
date：2021.8.27
key：
example：
输入：s = "00110"
输出：1
解释：我们翻转最后一位得到 00111.

输入：s = "010110"
输出：2
解释：我们翻转得到 011111，或者是 000111。
tips：
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt = {'0': 0, '1': 0}  # 记录 0 和 1 的出现次数
        times = 0

        for i in range(len(s)):
            cnt[s[i]] += 1
            # 若一开始为 0，将会被忽略，直到遍历到第一个 1 ，times才会大于 0
            # 如果 1 的次数比 0 要少，改 1 为 0 划算
            if cnt['0'] >= cnt['1']:
                times += cnt['1']
                cnt['1'], cnt['0'] = 0, 0

        # 处理最后一小段字符串可能全为 0 的情况
        return times + cnt['0']


if __name__ == '__main__':
    s = Solution()
    print(s.minFlipsMonoIncr("00011000"))
