class solution(object):
    def palin(self, x):
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        result = 0
        while x > result:
            result = result*10 + x%10
            x= x//10
            return x == result or x == result // 10
