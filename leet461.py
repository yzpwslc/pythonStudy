import string
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        zStr = str(bin(z))
        num = zStr.count('1')
        return num




def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            line = lines.next()
            y = stringToInt(line)

            ret = Solution().hammingDistance(x, y)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()