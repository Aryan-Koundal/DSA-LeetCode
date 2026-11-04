class Solution(object):
    def sortSentence(self, s):
        a = [""] * len(s.split())
        for i in s.split():
            b = int(i[-1]) - 1
            c = i[:-1]
            a[b] = c
        return " ".join(a)