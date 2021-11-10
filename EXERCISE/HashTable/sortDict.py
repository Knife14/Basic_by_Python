class Solution:
    def sort(self, s: str) -> str:
        res = {}
        res_l = []
        res_s = ""

        for i in list(s):
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

        res = sorted(res.items(), key=lambda x: x[1])
        # 此时的res是一个数组，而不是字典
        # sorted()函数返回的是一个数组
        for k, v in res:
            res_s += k
            res_s += str(v)

        return res_s


if __name__ == '__main__':
    s = Solution()
    print(s.sort("bcccdda"))