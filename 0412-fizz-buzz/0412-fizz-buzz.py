class Solution(object):
    def fizzBuzz(self, n):
        bucket = []
        for i in range (1,n+1):
             if (i%3==0)and(i%5==0):
                 bucket.append("FizzBuzz")
             elif (i%3==0):
                 bucket.append("Fizz")
             elif (i%5==0):
                 bucket.append("Buzz")
             else:
                a = str(i)
                bucket.append(a)
        return(bucket)
        