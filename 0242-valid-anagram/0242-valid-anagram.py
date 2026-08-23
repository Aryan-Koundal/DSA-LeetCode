class Solution(object):
    def isAnagram(self, s, t):
      count ={}
      count2 ={}
      for i in s:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
      for j in t:
        if j in count2:
            count2[j] +=1
        else:
            count2[j] =1
      if count == count2:
          return True
      else:
        return False
