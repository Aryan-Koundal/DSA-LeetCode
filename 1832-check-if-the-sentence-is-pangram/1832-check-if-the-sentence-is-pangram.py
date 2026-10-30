class Solution(object):
    def checkIfPangram(self, sentence):
        a = set(sentence)
        b = set("abcdefghijklmnopqrstuvwxyz")
        if a==b:
            return True 
        return False