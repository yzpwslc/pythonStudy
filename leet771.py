import re
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        pattern = '[' + J + ']{1,}'
        length0 = len(S)
        reg = re.compile(pattern)
        S = reg.sub('',S,0)
        length1 = len(S)
        return length0 - length1


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            J = stringToString(line)
            line = lines.next()
            S = stringToString(line)
            ret = Solution().numJewelsInStones(J, S)
            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()