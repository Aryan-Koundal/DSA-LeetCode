class Solution(object):
    def totalNumbers(self, digits):
          x = []
          for i in range(len(digits)):
            for j in range(len(digits)):
              if j !=i :
               for z in range(len(digits)):
                 if digits[i] != 0 and z !=j and digits[z]%2==0 and i!=z:
                   number = digits[i]*100 + digits[j]*10 +digits[z]
                   x.append(number)
          return len(set(x))