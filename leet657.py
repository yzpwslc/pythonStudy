import string
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        numU = moves.count('U')
        numD = moves.count('D')
        numL = moves.count('L')
        numR = moves.count('R')
        return (not bool(abs(numD - numU))) & (not bool(abs(numL - numR)))


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            moves = stringToString(line)

            ret = Solution().judgeCircle(moves)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()