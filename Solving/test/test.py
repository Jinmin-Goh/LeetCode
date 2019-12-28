class Solution(object):
    def fullJustify(self, words, maxWidth):
        # empty slots on the left will be assigned more spaces
        i = 0
        temp_cnt = 0
        temp_list = []
        ans = []
        while i < len(words):
            print(temp_cnt, temp_list)
            if temp_cnt + len(words[i]) <= maxWidth:
                temp_list.append(words[i])
                temp_cnt += len(words[i]) + 1
                
            else:
                None
            i += 1
        return [""]
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

def stringToStringArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def stringArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            words = stringToStringArray(line)
            line = lines.next()
            maxWidth = stringToInt(line)
            
            ret = Solution().fullJustify(words, maxWidth)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()