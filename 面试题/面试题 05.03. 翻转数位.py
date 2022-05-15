class Solution:
    def reverseBits(self, num: int) -> int:
        # 对二进制以“0”做分割
        cut_list = (
            bin(num)[2:].split("0")
            if num >= 0
            else bin(((1 << 32) - 1) & num)[2:].split("0")
        )
        cut_num = len(cut_list)
        # 二进制全“1”的情况，最前面可加“1”
        if cut_num == 1 and num >= 0:
            return len(cut_list[0]) + 1
        # 二进制全“1”的情况,负数的情况
        elif cut_num == 1 and num < 0:
            return len(cut_list[0])
        count = 1
        for i in range(0, cut_num - 1):
            count = max(count, len(cut_list[i]) + len(cut_list[i + 1]) + 1)
        return count


if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverseBits(9)
    print(ans)
