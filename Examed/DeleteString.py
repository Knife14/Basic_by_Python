"""
title：删除字符
writer：山客
date：2021.8.12
key：栈处理
example：
输入：
2
5 2
abcab
10 4
lkqijxsnny
输出：
aab
ijsnny
tips：
① 注意两处边界：遍历、返回
② 字典序小：即字符串中的字母尽可能满足升序
"""


def DeleteString(n: int, m: int, target: str):
    stack = []
    remove = []

    for t in target:
        # 边界条件：删除字符数量为 m 个
        # 删除标准：遍历到的当前元素，比栈顶元素ASCII码要小，
        #           故要删除栈顶元素，并且将当前元素压进栈中
        while len(stack) > 0 and len(remove) < m and t < stack[-1]:
            remove.append(stack.pop())
        stack.append(t)  # 压栈

    # 边界：res的长度 = 字符串原长度 n - 删除字符串长度 m
    return ''.join(stack[: n - m])


if __name__ == '__main__':
    T = int(input())  # T 组数据

    while T:
        tmp = list(map(int, input().split()))
        n, m = tmp[0], tmp[1]  # 该组字符串长度，可以删除字符数量
        target = input()

        res = DeleteString(n, m, target)
        print(res)

        # 循环条件
        T -= 1
