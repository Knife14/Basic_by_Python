"""
title：计算 K 位
writer：山客
date：2021.8.21
key：
example：
输入：
3 1
输出：
a
tips：
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回Sn的第k位字符
# @param n int整型 Sn的n
# @param k int整型 需要返回的字符下标位
# @return char字符型
#
class Solution:
    def findKthBit(self , n , k ):
        # write code here
        L = "abcdefghijklmnopqrstuvwxyz"  # 正序字母表
        rL = ''.join(list(reversed(L)))  # 翻转字母表

        def Invert(s: str):
            new = ""
            for i in range(len(s)):
                if s[i] == 'a':
                    new += 'z'
                elif s[i] == 'b':
                    new += 'y'
                elif s[i] == 'c':
                    new += 'x'
                elif s[i] == 'd':
                    new += 'w'
                elif s[i] == 'e':
                    new += 'v'
                elif s[i] == 'f':
                    new += 'u'
                elif s[i] == 'g':
                    new += 't'
                elif s[i] == 'h':
                    new += 's'
                elif s[i] == 'i':
                    new += 'r'
                elif s[i] == 'j':
                    new += 'q'
                elif s[i] == 'k':
                    new += 'p'
                elif s[i] == 'l':
                    new += 'o'
                elif s[i] == 'm':
                    new += 'n'
                elif s[i] == 'n':
                    new += 'm'
                elif s[i] == 'o':
                    new += 'l'
                elif s[i] == 'p':
                    new += 'k'
                elif s[i] == 'q':
                    new += 'j'
                elif s[i] == 'r':
                    new += 'i'
                elif s[i] == 's':
                    new += 'h'
                elif s[i] == 't':
                    new += 'g'
                elif s[i] == 'u':
                    new += 'f'
                elif s[i] == 'v':
                    new += 'e'
                elif s[i] == 'w':
                    new += 'd'
                elif s[i] == 'x':
                    new += 'c'
                elif s[i] == 'y':
                    new += 'b'
                elif s[i] == 'z':
                    new += 'a'

            return new

        S = ['a']
        for i in range(1, n):
            S.append(S[i - 1] + L[i] + ''.join(list(reversed(Invert(S[i - 1])))))

        return S[-1][k - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthBit(4, 11))
