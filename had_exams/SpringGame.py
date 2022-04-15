"""
title：字符游戏
writer：山客
date：2021.9.6
key：
example：
输入：
"aba"
输出：
3
tips：
① 目前通过率 7 / 11
    未通过案例为 199998（共20万个元素）
② 不能用回文
"""


class Solution:
    def solve(self, s):
        # write code here
        cnt = 0
        l, r = 0, len(s) - 1

        while l < len(s) and r > -1:
            if s[l] == s[r]:
                cnt += 1
                l += 1
                r -= 1
            else:
                break

        if cnt > 0:
            return cnt
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.solve("aa"))
