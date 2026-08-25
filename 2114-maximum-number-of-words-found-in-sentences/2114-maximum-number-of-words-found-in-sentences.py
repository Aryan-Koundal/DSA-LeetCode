class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        result =[]
        for i in sentences:
            result = i.split()
            if len(result)>count:
              count = len(result)
        return count

        