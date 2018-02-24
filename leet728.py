import json
import string
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        if left >= 1 and right <= 10000:
            ret = [num for num in range(left,right + 1) if selfDiv(num)]
        else:
            ret = []
        return ret


def selfDiv(num):

    strNum = str(num)
    if num >= 10:
        if strNum.find('0') < 0:
            lsNum = [int(i) for i in list(strNum)]
            setNum = set(lsNum)
            for i in setNum:
                if num % i != 0:
                    ret = False
                    break
                ret = True
        else:
            ret = False
    else:
        ret = True
    return ret

def stringToInt(input):
    return int(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            left = stringToInt(line)
            line = lines.next()
            right = stringToInt(line)

            ret = Solution().selfDividingNumbers(left, right)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()