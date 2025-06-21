class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        i, step = 0, 1

        for char in s:
            rows[i] += char
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step

        return "".join(rows)
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # "PINALSIGYAHRPI"
print(sol.convert("A", 1))               # "A"
